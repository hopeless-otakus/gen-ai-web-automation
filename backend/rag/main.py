import os
import uuid
import chromadb
from sentence_transformers import SentenceTransformer

# Use a clear path in the backend directory
CHROMA_DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db', 'chroma'))
os.makedirs(CHROMA_DB_PATH, exist_ok=True)
print(f"Storing ChromaDB at: {CHROMA_DB_PATH}")

# Use PersistentClient instead of Client
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Define the root directory for English content
root_directory = r"C:\Users\Paurush Kumar\Desktop\gen-ai-web-automation\backend\cerai-hugo\content\english"

# Clear existing collection if it exists
for collection in client.list_collections():
    if collection.name == "hugo_content":
        client.delete_collection("hugo_content")

# Create new collection
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

# Add verification after processing
print("\nVerifying database contents:")
print(f"Collection name: {collection.name}")
print(f"Collections available: {client.list_collections()}")

# Get all items from collection
all_results = collection.get()
print(f"\nTotal documents in collection: {len(all_results['ids'])}")
if len(all_results['ids']) > 0:
    print("\nSample document:")
    print(f"ID: {all_results['ids'][0]}")
    print(f"Metadata: {all_results['metadatas'][0]}")

# After processing, verify the files were created
print("\nVerifying ChromaDB files:")
for item in os.listdir(CHROMA_DB_PATH):
    print(f"- {item}")
