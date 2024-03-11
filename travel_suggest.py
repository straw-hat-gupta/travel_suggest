import streamlit as st
import cohere


# Initialize Cohere client with your API key
co = cohere.Client('v35Ph8kGEPe88xgfwopailwe9c6nR623gPGNFOta')


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

def suggest_location(modifiers):
    modifiers_str = ", ".join(modifiers)
    prompt = f"Suggest 1 travel location that matches the following attributes and list activities that match the attributes: {modifiers_str}"
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


# # Button to generate and display location suggestion
if st.button('Suggest Location'):
    if st.session_state['selected_modifiers']:
        location_suggestion = suggest_location(st.session_state['selected_modifiers'])
        st.write(f"Suggested travel location: {location_suggestion}")
    else:
        st.write("Please select at least one travel preference to get suggestions.")
