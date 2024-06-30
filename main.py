from embeddings.vector_database import initialize_vector_database, store_listings_in_database, semantic_search
import json

def load_listings(file_path):
    with open(file_path, 'r') as file:
        listings = json.load(file)
    
    # Optionally, you can validate each listing here
    for listing in listings:
        if 'Description' not in listing:
            raise ValueError(f"Listing {listing['Neighborhood']} is missing 'Description' field.")
    
    return listings

def main():
    client = initialize_vector_database()
    listings = load_listings('listings.json')  # Adjust path as necessary
    collection = store_listings_in_database(client, listings)

    user_query = input("Enter your preferences (e.g., 3 bedrooms, 2 bathrooms, Green Oaks, $800,000, backyard, modern kitchen): ")
    results = semantic_search(collection, user_query)

    for result in results:
        print(f"Matched Listing: {result['metadata']}")

if __name__ == "__main__":
    main()