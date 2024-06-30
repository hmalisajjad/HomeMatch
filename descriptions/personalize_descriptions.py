import openai
import json

openai.api_key = 'YOUR_OPENAI_API_KEY'

def personalize_listing_descriptions(listings, preferences):
    personalized_listings = []
    for listing in listings['matches']:
        prompt = f"""
        Here is a real estate listing:
        Description: {listing['metadata']['Description']}
        Neighborhood: {listing['metadata']['Neighborhood']}
        Preferences: {preferences}
        Rewrite the description to emphasize the buyer's preferences.
        """
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=150
        )
        personalized_description = response.choices[0].text.strip()
        listing['metadata']['Personalized Description'] = personalized_description
        personalized_listings.append(listing['metadata'])
    return personalized_listings