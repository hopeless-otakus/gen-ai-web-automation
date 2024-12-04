from hug_chat import HugChat
from mapping import Mapping
import chromadb
from sentence_transformers import SentenceTransformer
import subprocess
import sys
import json
import os

CHROMA_DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db', 'chroma'))

def get_rag_context(prompt, category, fields):
    try:
        print(f"Querying RAG with prompt: {prompt}, category: {category}")
        client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        collection = client.get_collection("hugo_content")
        
        # Generate embedding for the query using the same model as in main.py
        model = SentenceTransformer('all-MiniLM-L6-v2')
        query_embedding = model.encode(prompt).tolist()
        
        # Query the collection using embeddings
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3,
            where={"tag": category}
        )
        
        context = ""
        if results and results['metadatas']:
            valid_docs = []
            for metadata in results['metadatas'][0]:
                if metadata and 'file' in metadata:
                    valid_docs.append(metadata['file'])
            
            print(f"Found {len(valid_docs)} valid documents")
            if valid_docs:
                context = "\n---\n".join(valid_docs)
        
        if not context:
            print("No valid context found, using default template")
            context = f"This is a {category} entry with fields: {', '.join(fields)}"
        
        return context.strip()
    except Exception as e:
        print(f"RAG Error: {e}")
        print("Using fallback context")
        return f"Example {category} entry with required fields"

def get_llm_response(prompt, category, fields):
    try:
        chatbot = HugChat()
        rag_context = get_rag_context(prompt, category, fields)
        
        # First set the context and role
        context_prompt = f"""You are a structured data extractor. You will receive markdown files and a user query.
Your task is to extract specific fields from the query in the same format as the markdown files.
Here are example markdown files for reference:

{rag_context}

Focus only on extracting the required fields: {', '.join(fields)}"""
        
        chatbot.chat(context_prompt)
        
        # Then ask for specific JSON extraction
        extraction_prompt = f"""From this text: "{prompt}"
Create a JSON object with ONLY these fields: {', '.join(fields)}
- Use null for missing fields
- Format dates as YYYY-MM-DD
- Only use information explicitly stated
- Do not make up or infer any data

Return ONLY the JSON object, no other text."""
        
        response = chatbot.chat(extraction_prompt)
        print("\nRaw LLM response:", response)
        
        # Clean and parse response
        response_text = str(response)
        json_str = response_text[response_text.find('{'):response_text.rfind('}')+1]
        
        if not json_str:
            print("No JSON found in response")
            return None
            
        try:
            parsed = json.loads(json_str)
            print("\nExtracted fields:", json.dumps(parsed, indent=2))
            return parsed
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            return None
            
    except Exception as e:
        print(f"Error in LLM response: {e}")
        return None

def handle_natural_language_prompt(prompt):
    mapping = Mapping()
    categories = mapping.get_categories()
    
    # Category detection
    prompt_lower = prompt.lower()
    category_matches = [
        cat for cat in categories 
        if cat in prompt_lower or f"new {cat}" in prompt_lower or f"add {cat}" in prompt_lower
    ]
    
    if not category_matches:
        return "Could not determine category. Please specify one of: " + ", ".join(categories)
    
    category = category_matches[0]
    fields = mapping.get_category_fields(category)
    
    # Extract fields using LLM
    field_values = get_llm_response(prompt, category, fields)
    
    if not field_values:
        return "Could not extract fields from prompt"
    
    # Execute command with extracted fields
    cmd = [sys.executable, "crud_interface.py", category]
    for field, value in field_values.items():
        if value:
            cmd.extend([f"--{field}", str(value)])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    sample_prompt = "create an event title AI breakout happening on 2022-10-15 at KFC plaza and line for this is www.example.com"
    print(handle_natural_language_prompt(sample_prompt))