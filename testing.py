import cohere
import requests
import re

# Initialize Cohere client with your API key
co = cohere.Client('v35Ph8kGEPe88xgfwopailwe9c6nR623gPGNFOta')

# Google Custom Search JSON API information
google_api_key = "AIzaSyD5bmhlMmUWcoRQ_ErFPm3M_8iMA5b28Pg"
search_engine_id = "c7a913be38bf742dc"

def extract_location(suggestion):
    # Pattern to match the location name after the known starting text.
    # It captures the location name following the 'is' and before the period.
    lines = suggestion.split('\n')
    if lines:
        location = lines[0].strip()  # Remove any leading/trailing whitespace
        return location
    else:
        return ""
    
    # Function to suggest a location based on selected modifiers using Cohere
def suggest_location(modifiers):
    modifiers_str = ", ".join(modifiers)
    prompt = f"Suggest 1 travel location that matches the following attributes and list activities that match the attributes: {modifiers_str}. always have the name of the location at the top."
    response = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=500,  # Adjust as needed
        temperature=0.75,  # Adjust for creativity
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0
        # stop_sequences=["\n"],  # Stop generating further if it reaches a newline
    )
    return response.generations[0].text.strip()

#  Function to search for an image based on the suggested location
def search_image(query):
    search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={search_engine_id}&searchType=image&key={google_api_key}"
    response = requests.get(search_url)
    if response.status_code == 200:
        results = response.json()
        image_url = results['items'][0]['link']
        return image_url
    else:
        return None