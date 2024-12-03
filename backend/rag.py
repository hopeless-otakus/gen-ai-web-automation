import os
from sentence_transformers import SentenceTransformer
import chromadb
from hug_chat import HugChat
import json

CHROMA_DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db', 'chroma'))
print(f"Loading ChromaDB from: {CHROMA_DB_PATH}")

if not os.path.exists(CHROMA_DB_PATH):
    print(f"ERROR: ChromaDB directory not found at {CHROMA_DB_PATH}")
    print("Please run main.py first to create and populate the database.")
    exit(1)

client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
model = SentenceTransformer('all-MiniLM-L6-v2')
chatbot = HugChat()

collection = client.get_collection("hugo_content")

all_results = collection.get()
print(f"\nChromaDB Status:")
print(f"Collection name: {collection.name}")
print(f"Total documents: {len(all_results['ids'])}")

if len(all_results['ids']) == 0:
    print("WARNING: Collection is empty! Run main.py first to populate the database.")

print("Rag model loaded successfully.")

def extract_context(prompt):
  query_embedding = model.encode(prompt)
  results = collection.query(query_embeddings=[query_embedding.tolist()], n_results=3)
  
  print(f"Query results: {results}")  # Debug print
  
  response_data = []
  for metadata_list in results['metadatas']:
      for result in metadata_list:
          response_data.append({
              "tag": result['tag'],
              "content": result['file']
          })
  
  context = chatbot.chat(f"rewrite the following extract in a descriptive and human understandable manner: \n {json.dumps(response_data)}")
  return context

# prompt = "Please create an event titled 'Test Event' on 21/21/21 at the venue 'something'. The event image is 'asd.png' and you can find more details at the link 'something'."
# result = extract_context(prompt)
# print(result)
  