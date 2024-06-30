from preferences.user_preferences import collect_buyer_preferences
from embeddings.vector_database import initialize_vector_database, store_listings_in_database, semantic_search
from descriptions.personalize_descriptions import personalize_listing_descriptions
import json

def main():
    # Load listings
    with open('data/listings.json', 'r') as f:
        listings = json.load(f)
    
    # Initialize the vector database for storing listings
    initialize_vector_database()
    store_listings_in_database(listings)
    
    # Collect the buyer preferences
    buyer_preferences = collect_buyer_preferences()
    
    # searching to find matching listings
    matched_listings = semantic_search(buyer_preferences)
    
    # Personalize the descriptions of the matched listings
    personalized_listings = personalize_listing_descriptions(matched_listings, buyer_preferences)
    
    # Display personalized listings for user
    display_personalized_listings(personalized_listings)

def display_personalized_listings(personalized_listings):
    for idx, listing in enumerate(personalized_listings):
        print(f"Listing {idx + 1}:")
        print("Neighborhood:", listing["Neighborhood"])
        print("Price:", listing["Price"])
        print("Bedrooms:", listing["Bedrooms"])
        print("Bathrooms:", listing["Bathrooms"])
        print("House Size:", listing["House Size"])
        print("Original Description:", listing["Description"])
        print("Personalized Description:", listing.get("Personalized Description", "N/A"))
        print("Neighborhood Description:", listing["Neighborhood Description"])
        print("\n")

if __name__ == '__main__':
    main()