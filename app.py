import streamlit as st
import requests
from streamlit_image_select import image_select

# Dictionary of actors, their corresponding video URLs, and image URLs
ACTOR_VIDEOS = {
    "Original": {
        "video_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/opp.mp4",
        "image_url": "https://github.com/AI-ANK/bmjoanisawful/raw/cf49344156010790d3a3ca56f66c1ee5de7060a4/images/jimmy.jpg",
    },
    "Actor 1": {
        "video_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/download.mp4",
        "image_url": "https://github.com/AI-ANK/bmjoanisawful/raw/cf49344156010790d3a3ca56f66c1ee5de7060a4/images/john.jpg",
    },
    "Actor 2": {
        "video_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/download.mp4",
        "image_url": "https://github.com/AI-ANK/bmjoanisawful/raw/cf49344156010790d3a3ca56f66c1ee5de7060a4/images/joaquin.jpg",
    },
    # Add more actors and their corresponding videos and images
}

# Legal Disclaimer Button
if st.button('View Legal Disclaimer'):
    st.warning("""
    **Legal Disclaimer**
    This demonstration is intended solely for...
    ... [continue the rest of the disclaimer here]
    """)

# Title of the app
st.title("Choose Your Actor")

# Display actor images for selection
actor_names = list(ACTOR_VIDEOS.keys())
actor_images = [ACTOR_VIDEOS[actor]['image_url'] for actor in actor_names]

selected_index = image_select(
    "",
    images=actor_images,
    captions=actor_names,
    index=0,
    return_value="index",
)

# Use the selected index to get the video URL
selected_video_url = ACTOR_VIDEOS[actor_names[selected_index]]["video_url"]

# Check if the video URL is valid
response = requests.head(selected_video_url)
if response.status_code == 200:
    st.video(selected_video_url)
else:
    st.error("Video not found. Please check the URL.")
