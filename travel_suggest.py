import streamlit as st
import cohere
import requests
import re

# Backend

# Initialize Cohere client with your API key
co = cohere.Client('v35Ph8kGEPe88xgfwopailwe9c6nR623gPGNFOta')

# Google Custom Search JSON API information
google_api_key = "AIzaSyD5bmhlMmUWcoRQ_ErFPm3M_8iMA5b28Pg"
search_engine_id = "c7a913be38bf742dc"


# Function to suggest a location based on selected modifiers using Cohere
def suggest_location(modifiers):
    modifiers_str = ", ".join(modifiers)
    prompt = f"Suggest 1 travel location that matches the following attributes and list activities that match the attributes: {modifiers_str}. always have the name of the location at the top."
    response = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=500,
        temperature=0.75,  # Adjust for creativity
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.generations[0].text.strip()

def extract_location(suggestion):
    lines = suggestion.split('\n')
    if lines:
        location = lines[0].strip()  # Remove any leading/trailing whitespace
        return location
    else:
        return ""
    
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


# Frontend

# Title of the application
st.title('Travel Suggester')

# Define travel preferences
travel_modifiers = [
    'Beach', 'Mountains', 'City', 'Nature', 'Historical',
    'Adventure', 'Relaxation', 'Cultural', 'Cuisine'
]

# Define the number of columns for your grid
num_columns = 3

# Initialize the selected travel preferences state
if 'selected_modifiers' not in st.session_state:
    st.session_state['selected_modifiers'] = []

# Function to handle button click
def button_pressed(modifier):
    if modifier in st.session_state['selected_modifiers']:
        st.session_state['selected_modifiers'].remove(modifier)
    else:
        st.session_state['selected_modifiers'].append(modifier)

# Create the grid of buttons
for i in range(0, len(travel_modifiers), num_columns):
    cols = st.columns(num_columns)  # Create a row of columns
    for j in range(num_columns):
        idx = i + j
        if idx < len(travel_modifiers):
            modifier = travel_modifiers[idx]
            button_key = f'button_{modifier}'
            # Place a button in each column
            if cols[j].button(modifier, key=button_key):
                button_pressed(modifier)

# Display selected modifiers
st.write('Selected Modifiers:', ', '.join(st.session_state['selected_modifiers']))

# Button to generate and display location suggestion and image
if st.button('Suggest Location'):
    if st.session_state['selected_modifiers']:
        location_suggestion = suggest_location(st.session_state['selected_modifiers'])
        
        location = extract_location(location_suggestion)
        # Fetch and display the image for the suggested location
        image_url = search_image(location)
        if image_url:
            st.image(image_url, caption=f"Image of {location} \n")
        else:
            st.write("No image available for this location.")

        st.write(f"Suggested travel location: {location_suggestion}")
    else:
        st.write("Please select at least one travel preference to get suggestions.")
