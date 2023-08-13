import streamlit as st
import requests

# Dictionary of actors and their corresponding video URLs
ACTOR_VIDEOS = {
    "Original": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/opp.mp4",
    "Actor 1": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/download.mp4",
    "Actor 2": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/download.mp4",
    # Add more actors and their corresponding videos
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
st.title("Choose Your Actor")

# Dropdown for selecting an actor
selected_actor = st.selectbox("Select an Actor:", options=list(ACTOR_VIDEOS.keys()))

# Display the selected video
video_url = ACTOR_VIDEOS[selected_actor]

# Check if the video URL is valid
response = requests.head(video_url)
if response.status_code == 200:
    st.video(video_url)
else:
    st.error("Video not found. Please check the URL.")
