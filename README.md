# travel_suggest

## Overview
The Travel Suggester App is a lightweight web application built using Streamlit and Cohere's powerful AI API. This project was conceived and developed within a timeframe of under 3 hours, demonstrating rapid learning and implementation skills with no prior experience using the Cohere API.

## Description of the Project
The Travel Suggester App aims to provide users with personalized travel destination suggestions based on their preferences such as climate, geography, and activities. By selecting various travel modifiers like "beach", "historical", or "mountains", the user can tailor their search to fit their ideal vacation scenario. Upon submission, the app uses Cohere's AI to generate a specific travel location along with a list of recommended activities unique to that destination.

This application showcases the integration of Cohere's text generation capabilities, offering a seamless and interactive user experience. The project further explores dynamic image fetching based on the suggested location to enhance the visual appeal and provide users with a glimpse of their potential travel destination.

### Backend <br/>
- Cohere Client Initialization: Sets up the Cohere client with your API key, ready to use its capabilities for generating text based on prompts.
- Location Suggestion Function (suggest_location): Takes user-selected travel preferences, forms a prompt, and gets a suggestion from Cohere's model. It's designed to ensure the location name is at the top of the generated text for easy extraction.
- Image Search Function (search_image): Uses Google's Custom Search JSON API to find an image related to the suggested location. It constructs a search URL with the query being the location name, sends a request, and handles the response by extracting the first image's URL.
### Frontend <br/>
- Travel Modifiers Setup: Defines a list of travel preferences and dynamically generates a grid of buttons for the user to select their interests.
- Location Suggestion and Image Display: Once the user finalizes their preferences and requests a location suggestion, the application:
-- Generates a travel suggestion using Cohere.
-- Extracts the location name from the suggestion.
-- Fetches and displays an image related to the location.
-- Shows the detailed suggestion text, including activities.

## Reasons for Creating the Project
- Quick Learning Demonstrated: This project was an opportunity to prove the ability to quickly grasp and effectively implement new technologies. Despite having no previous experience with Cohere's API, the development of a fully functional application in a short period highlights a strong aptitude for learning and adaptation. <br/>
- Showcasing Cohere API's Ease of Use: Cohere's API is not only powerful but also incredibly user-friendly. This project serves to illustrate how straightforward it is to develop with Cohere, enabling even those new to the API to create something meaningful and fun.<br/>
Personal Challenge: The motivation behind this project was not just to build something for a job application but also to challenge personal development skills. It stands as a testament to the ability to conceptualize, design, and execute a software project rapidly.<br/>
- Aspiring to Be an Asset to the Cohere Team: This project was driven by a desire to join the Cohere team. It demonstrates a proactive approach to learning and using Cohere's technology, highlighting potential contributions to the team with innovative thinking and technical proficiency.<br/>



## Conclusion
The Travel Suggester App is a simple yet effective demonstration of what can be achieved with a powerful AI tool like Cohere's API, combined with a fast learning curve and a passion for tackling new challenges. It reflects a commitment to innovation, continuous learning, and the desire to contribute meaningfully to a team that's at the forefront of AI technology.
