import streamlit as st
import requests
from streamlit_image_select import image_select

REPO_OWNER = "AI-ANK"
REPO_NAME = "bmjoanisawful"
VIDEO_FOLDER_PATH = "videos"
IMAGE_FOLDER_PATH = "images"
DEFAULT_IMAGE_URL = "url_of_default_image.jpg"  # replace with your default image URL

# Fetch files from GitHub repo's 'videos' folder
video_files_response = requests.get(f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{VIDEO_FOLDER_PATH}")
video_files = [file['name'] for file in video_files_response.json()]

# Initialize actor_videos dictionary
ACTOR_VIDEOS = {}

# Populate ACTOR_VIDEOS with video URLs and corresponding image URLs
for video_file in video_files:
    actor_name = video_file.split('.')[0]  # assuming file names without dots except for the extension
    video_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/raw/main/{VIDEO_FOLDER_PATH}/{video_file}"
    
    # Check if corresponding image exists
    image_file = f"{actor_name}.jpg"  # assuming image format is jpg
    image_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/raw/main/{IMAGE_FOLDER_PATH}/{image_file}"
    response = requests.head(image_url)
    if response.status_code != 200:
        image_url = DEFAULT_IMAGE_URL
    
    ACTOR_VIDEOS[actor_name] = {
        "video_url": video_url,
        "image_url": image_url,
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
