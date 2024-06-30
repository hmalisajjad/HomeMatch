def collect_buyer_preferences():
    preferences = {}
    preferences['Bedrooms'] = input("How many bedrooms do you want? ")
    preferences['Bathrooms'] = input("How many bathrooms do you need? ")
    preferences['Location'] = input("What is your preferred location? ")
    preferences['Budget'] = input("What is your budget (e.g., $500,000)? ")
    preferences['Amenities'] = input("What amenities are important to you (e.g., backyard, modern kitchen)? ")
    return preferences