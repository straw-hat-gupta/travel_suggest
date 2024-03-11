import cohere


# Initialize Cohere client with your API key
co = cohere.Client('v35Ph8kGEPe88xgfwopailwe9c6nR623gPGNFOta')


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

modifiers = ['Beach', 'Mountains', 'City', 'Nature']

location_suggestion = suggest_location(modifiers)
print(location_suggestion)