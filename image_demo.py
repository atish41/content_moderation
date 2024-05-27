import streamlit as st
import http.client
import json
from pprint import pprint 

# Define the image_analysis function
def image_analysis(img_url: str, userId: int, postId: int, metadata: dict, doNotStore: bool = True) -> dict:
    """
    Analyzes an image for inappropriate content.

    Args:
        img_url (str): The URL of the image to be analyzed.
        userId (int): User ID of the user.
        postId (int): Post ID of the content.
        metadata (dict): Any extra information to be provided.
        doNotStore (bool): Whether to store the content. If set to True, the content won't enter the review queue.

    Returns:
        dict: The result of the image analysis.
    """
    conn = http.client.HTTPSConnection("moderationapi.com")

    payload = {
        "doNotStore": doNotStore,
        "authorId": str(userId),
        "contextId": str(postId),
        "metadata": metadata,
        "url": img_url
    }

    data = json.dumps(payload).encode('utf-8')
    headers = {
        "Authorization": "Bearer proj_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2NDViMjIzNmE4OTgxN2RhMTM1ZDdlOSIsInVzZXJJZCI6IjY2NDRlNTkyODA0MTIxNDUyYjgyMTc0MSIsInRpbWVzdGFtcCI6MTcxNTg0MzYxOTAzNiwiaWF0IjoxNzE1ODQzNjE5fQ.Zs3E6L7qLZVmIOU3yfeYS0dmmqAISYtAb6190dZ17lE",
        "Content-Type": "application/json"
    }
    conn.request("POST", "/api/v1/moderate/image", data, headers)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    return json.loads(data)

# Title of the application
st.title("Image Moderation App")

# Image URL input
img_url = st.text_input(label="Enter Image URL")

# Display the image if the URL is provided
if img_url:
    st.markdown(f"![Alt Text]({img_url})")

# Post ID input
post_id = st.text_input(label="Enter Post ID")

# User ID input
user_id = st.text_input(label="Enter User ID")

# A button to trigger the analysis
if st.button('Analyze Image'):
    # Validate input fieldshh
    if not img_url or not post_id or not user_id:
        st.error("Please provide all required inputs: Image URL, Post ID, and User ID.")
    else:
        try:
            # Call the image analysis function
            res = image_analysis(img_url, int(user_id), int(post_id), {})

            # Display the results
            st.write("Inappropriate:", res['flagged'])
            st.write(res)
        except Exception as e:
            st.error(f"An error occurred: {e}")
