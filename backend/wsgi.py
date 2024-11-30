import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from sentence_transformers import SentenceTransformer
import chromadb

# Use the same path as main.py
CHROMA_DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db', 'chroma'))
print(f"Loading ChromaDB from: {CHROMA_DB_PATH}")

if not os.path.exists(CHROMA_DB_PATH):
    print(f"ERROR: ChromaDB directory not found at {CHROMA_DB_PATH}")
    print("Please run main.py first to create and populate the database.")
    exit(1)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://localhost:1313"], "supports_credentials": True}})

# Use PersistentClient instead of Client
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Get the collection
collection = client.get_collection("hugo_content")

# Verify collection contents
all_results = collection.get()
print(f"\nChromaDB Status:")
print(f"Collection name: {collection.name}")
print(f"Total documents: {len(all_results['ids'])}")

if len(all_results['ids']) == 0:
    print("WARNING: Collection is empty! Run main.py first to populate the database.")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    prompt = data.get('prompt')
    print(f"Received prompt: {prompt}")

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
    
    print(f"Sending response: {response_data}")  # Debug print
    return jsonify({"message": response_data})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)