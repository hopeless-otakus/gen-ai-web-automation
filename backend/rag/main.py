import os
import uuid
import chromadb
from sentence_transformers import SentenceTransformer

# Initialize Chroma client and SentenceTransformer model
client = chromadb.Client()
model = SentenceTransformer('all-MiniLM-L6-v2')

# Define the root directory for English content
root_directory = r"C:\Users\Paurush Kumar\Desktop\gen-ai-web-automation\backend\cerai-hugo\content\english"

# Create a Chroma collection
collection = client.create_collection("hugo_content")

# Function to process and store markdown files
def process_markdown_files():
    # Loop through all subdirectories in the 'english' folder
    for subdir in os.listdir(root_directory):
        subdir_path = os.path.join(root_directory, subdir)
        
        # Check if it's a directory
        if os.path.isdir(subdir_path):
            print(f"Processing folder: {subdir}")
            
            # Loop through all files in the subdirectory
            for filename in os.listdir(subdir_path):
                if filename.endswith(".md"):
                    # Read the markdown file content
                    file_path = os.path.join(subdir_path, filename)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        markdown_content = file.read()

                    # Generate embedding for the file content
                    embedding = model.encode(markdown_content)

                    # Add the document to Chroma
                    document_id = str(uuid.uuid4())  # Unique ID
                    metadata = {"tag": subdir, "file": markdown_content}

                    collection.add(
                        ids=[document_id],
                        embeddings=[embedding.tolist()],
                        metadatas=[metadata]
                    )

# Run the processing function
process_markdown_files()

# Example query to retrieve documents
# Example query to retrieve documents
query = "AI seminar event details"
query_embedding = model.encode(query)

# Retrieve relevant documents from Chroma
results = collection.query(query_embeddings=[query_embedding.tolist()], n_results=3)

# Iterate through the nested list of metadata
for metadata_list in results['metadatas']:
    for result in metadata_list:  # Each `metadata_list` contains individual metadata dictionaries
        print(f"Tag: {result['tag']}")
        print(f"Content: {result['file'][:200]}...")


import pprint
pprint.pprint(results['metadatas'])
