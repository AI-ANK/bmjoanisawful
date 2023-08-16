import streamlit as st
import requests

# Dictionary of actors, their corresponding video URLs, and image URLs
ACTOR_VIDEOS = {
    "Original": {
        "video_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/opp.mp4",
        "image_url": "url_of_original_actor_image.jpg",
    },
    "Actor 1": {
        "video_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/download.mp4",
        "image_url": "url_of_actor1_image.jpg",
    },
    "Actor 2": {
        "video_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/download.mp4",
        "image_url": "url_of_actor2_image.jpg",
    },
    # Add more actors and their corresponding videos and images
}

# Legal Disclaimer Button
if st.button('View Legal Disclaimer'):
    st.warning("""
    **Legal Disclaimer**
    This demonstration is intended solely for educational and learning purposes. The videos, images, and other content used in this demonstration are the intellectual property of their respective owners. This demonstration does not claim any ownership over these materials and is not intended for commercial use.
    The use of copyrighted material in this demonstration is believed to fall under the "fair use" doctrine, as it is used for educational purposes, is non-commercial in nature, and does not materially affect the potential market for or value of the copyrighted work. Nevertheless, if you are a copyright holder and believe that any content used in this demonstration infringes upon your rights, please contact us at [your contact information here], and we will promptly address your concerns.
    By accessing this demonstration, you acknowledge and agree that you understand the nature of this demonstration and that you will not use it for any unlawful or prohibited purposes. The creators of this demonstration make no representations or warranties regarding the accuracy, legality, or completeness of the content and disclaim all liability for any damages arising from the use of this demonstration.
    """)

# Title of the app
st.title("Choose Your Actor V2")

# Default video (can be the original or any other default choice)
selected_video_url = ACTOR_VIDEOS["Original"]["video_url"]

# Display images of actors for selection
for actor, details in ACTOR_VIDEOS.items():
    if st.image(details["image_url"], caption=actor, width=100, use_column_width=False):
        selected_video_url = details["video_url"]

# Check if the video URL is valid
response = requests.head(selected_video_url)
if response.status_code == 200:
    st.video(selected_video_url)
else:
    st.error("Video not found. Please check the URL.")
