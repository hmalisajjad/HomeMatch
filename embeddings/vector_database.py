from chromadb import Client
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

def initialize_vector_database():
    client = Client(Settings())
    return client

def store_listings_in_database(client, listings):
    collection = client.create_collection("listings")

    for listing in listings:
        embedding = generate_embedding(listing['description'])
        collection.add_document({
            'id': listing['id'],
            'embedding': embedding,
            'metadata': listing
        })

    return collection

def generate_embedding(text):
    # Use a generic embedding function from ChromaDB or another library
    embedding_function = embedding_functions.default_embedding_function()
    return embedding_function.embed(text)

def semantic_search(collection, query):
    embedding = generate_embedding(query)
    results = collection.search(embedding, limit=5)
    return results