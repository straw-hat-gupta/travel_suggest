import streamlit as st


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




# Button to generate and display location suggestion
if st.button('Suggest Location'):
    if st.session_state['selected_modifiers']:
        location_suggestion = 'Dummy, Dummyland'
        st.write(f"Suggested travel location: {location_suggestion}")
    else:
        st.write("Please select at least one travel preference to get suggestions.")

