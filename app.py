import streamlit as st
import requests
from streamlit_image_select import image_select
from PIL import Image
import io
import os

st.markdown(
    '''
    <style>
        .imageSelect img {
            display: inline-block !important;
            width: auto !important;
            max-width: 100%;
        }
        .imageSelect {
            white-space: nowrap;
            overflow-x: auto;
        }
    </style>
    ''',
    unsafe_allow_html=True,
)

# Dictionary of actors, their corresponding video URLs, and image URLs
ACTOR_VIDEOS = {
    "Original": {
        "video_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/videos/office.mp4",
        "image_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/images/ms.jpg",
    },
    "John Cena": {
        "video_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/videos/1jcf.mp4",
        "image_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/images/1jc.jpg",
    },
    "Joaquin Phoenix": {
        "video_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/videos/1jpf.mp4",
        "image_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/images/1jp.jpg",
    },
    "Mr Beast": {
        "video_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/videos/1mrbf.mp4",
        "image_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/images/1mrb.jpg",
    },
    "Bob Odenkirk": {
        "video_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/videos/1sgf.mp4",
        "image_url": "https://cdn.jsdelivr.net/gh/AI-ANK/bmjoanisawful@main/images/1sg.jpg",
    },
}

# Define actor_names right after ACTOR_VIDEOS
actor_names = list(ACTOR_VIDEOS.keys())

# Legal Disclaimer Button
if st.button('View Legal Disclaimer'):
    st.warning("""
     **Legal Disclaimer**
    This demonstration is intended solely for educational and learning purposes. The videos, images, and other content used in this demonstration are the intellectual property of their respective owners. This demonstration does not claim any ownership over these materials and is not intended for commercial use.
    The use of copyrighted material in this demonstration is believed to fall under the "fair use" doctrine, as it is used for educational purposes, is non-commercial in nature, and does not materially affect the potential market for or value of the copyrighted work. Nevertheless, if you are a copyright holder and believe that any content used in this demonstration infringes upon your rights, please contact us at [your contact information here], and we will promptly address your concerns.
    By accessing this demonstration, you acknowledge and agree that you understand the nature of this demonstration and that you will not use it for any unlawful or prohibited purposes. The creators of this demonstration make no representations or warranties regarding the accuracy, legality, or completeness of the content and disclaim all liability for any damages arising from the use of this demonstration.
    """)

# Create columns for each actor image
columns = st.columns(len(ACTOR_VIDEOS))

selected_actor = None
for idx, (actor, details) in enumerate(ACTOR_VIDEOS.items()):
    with columns[idx]:
        if st.button("", image=details["image_url"]):
            selected_actor = actor

# If an actor's image is clicked, update the video URL
if selected_actor:
    selected_video_url = ACTOR_VIDEOS[selected_actor]["video_url"]
else:  # Default to "Original" if no actor is selected yet
    selected_video_url = ACTOR_VIDEOS["Original"]["video_url"]

# Check if the video URL is valid
response = requests.head(selected_video_url)
if response.status_code == 200:
    st.markdown(f'<video width="100%" controls autoplay src="{selected_video_url}"></video>', unsafe_allow_html=True)
else:
    st.error("Video not found. Please check the URL.")
