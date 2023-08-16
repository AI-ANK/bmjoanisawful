import streamlit as st
import requests
from streamlit_image_select import image_select

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

# Legal Disclaimer Button
if st.button('View Legal Disclaimer'):
    st.warning("""
     **Legal Disclaimer**
    This demonstration is intended solely for educational and learning purposes. The videos, images, and other content used in this demonstration are the intellectual property of their respective owners. This demonstration does not claim any ownership over these materials and is not intended for commercial use.
    The use of copyrighted material in this demonstration is believed to fall under the "fair use" doctrine, as it is used for educational purposes, is non-commercial in nature, and does not materially affect the potential market for or value of the copyrighted work. Nevertheless, if you are a copyright holder and believe that any content used in this demonstration infringes upon your rights, please contact us at [your contact information here], and we will promptly address your concerns.
    By accessing this demonstration, you acknowledge and agree that you understand the nature of this demonstration and that you will not use it for any unlawful or prohibited purposes. The creators of this demonstration make no representations or warranties regarding the accuracy, legality, or completeness of the content and disclaim all liability for any damages arising from the use of this demonstration.
    """)

# Determine screen width to adjust layout
screen_width = st.session_state.get("screen_width", 0)
if not screen_width:
    st.write("<script>window.onload = function() { var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0); parent.parent.postMessage({'screen_width': w}, '*'); }</script>", unsafe_allow_html=True)
    st.stop()
else:
    st.session_state.screen_width = 0  # Reset for next load

st.title("Choose Your Actor")

# Placeholder for the video
video_placeholder = st.empty()

# Display actor images for selection
actor_names = list(ACTOR_VIDEOS.keys())
actor_images = [ACTOR_VIDEOS[actor]['image_url'] for actor in actor_names]

# Adjust layout based on screen width
if screen_width > 480:  # Desktop or large tablet
    cols = st.beta_columns(len(actor_names))
else:  # Mobile or small screen
    cols = st.beta_columns([1] * min(len(actor_names), 3))  # 3 images per row

selected_actor = None
for i, actor in enumerate(actor_names):
    if cols[i % len(cols)].image(actor_images[i], caption=actor, use_column_width=True, width=None if screen_width <= 480 else 100):
        selected_actor = actor

# If an actor is selected, play the video
if selected_actor:
    video_url = ACTOR_VIDEOS[selected_actor]['video_url']
    video_placeholder.markdown(f'<video width="100%" controls autoplay src="{video_url}"></video>', unsafe_allow_html=True)
