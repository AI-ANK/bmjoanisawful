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

# If session state doesn't have the selected_index yet, initialize it to 0 (default)
if 'selected_index' not in st.session_state:
    st.session_state['selected_index'] = 0

# Use the current session state's selected_index to get the video URL
selected_video_url = ACTOR_VIDEOS[actor_names[st.session_state['selected_index']]]["video_url"]

# Check if the video URL is valid and display it
response = requests.head(selected_video_url)
if response.status_code == 200:
    st.markdown(f'<video width="100%" controls autoplay src="{selected_video_url}"></video>', unsafe_allow_html=True)
else:
    st.error("Video not found. Please check the URL.")

# Display actor images for selection
actor_names = list(ACTOR_VIDEOS.keys())
actor_images = [ACTOR_VIDEOS[actor]['image_url'] for actor in actor_names]

# Use image_select to get the index of the clicked actor's image
clicked_index = image_select(
    "",
    images=actor_images,
    captions=actor_names,
    index=st.session_state['selected_index'],  # Use the session state's selected index as the default
    return_value="index",
    use_container_width=0,
)

# If the clicked index is different from the current selected_index, update the session state
if clicked_index != st.session_state['selected_index']:
    st.session_state['selected_index'] = clicked_index
