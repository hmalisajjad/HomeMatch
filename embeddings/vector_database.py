import chromadb
from chromadb.utils.embedding_functions import openai_embedding
import json

client = None
collection = None

def initialize_vector_database():
    global client, collection
    client = chromadb.Client()
    collection = client.create_collection("real_estate")

def store_listings_in_database(listings):
    for idx, listing in enumerate(listings):
        embedding = openai_embedding.embed_text(json.dumps(listing))
        collection.insert(
            data_id=f"listing_{idx}",
            vector=embedding,
            metadata=listing
        )

def semantic_search(preferences):
    query = json.dumps(preferences)
    query_embedding = openai_embedding.embed_text(query)
    results = collection.query(query_embedding, top_k=5)
    return results