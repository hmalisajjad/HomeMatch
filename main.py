import os
import json
from embeddings.vector_database import initialize_vector_database, store_listings_in_database, semantic_search

def load_listings(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found. Please check the file path and try again.")
    
    with open(file_path, 'r') as file:
        listings = json.load(file)
    
    # Optionally, you can validate each listing here
    for listing in listings:
        if 'description' not in listing:
            raise ValueError(f"Listing {listing['Neighborhood']} is missing 'description' field.")
    
    return listings

def main():
    client = initialize_vector_database()
    listings_file = 'listings.json'  # Adjust file name as necessary
    listings_path = os.path.join('D:\\udacity students projects\\HomeMatch\\data', listings_file)  # Adjust directory path as necessary
    listings = load_listings(listings_path)
    collection = store_listings_in_database(client, listings)

    user_query = input("Enter your preferences (e.g., 3 bedrooms, 2 bathrooms, Green Oaks, $800,000, backyard, modern kitchen): ")
    results = semantic_search(collection, user_query)

    for result in results:
        print(f"Matched Listing: {result['metadata']}")

if __name__ == "__main__":
    main()