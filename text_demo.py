import streamlit as st
import http.client
import json

# Define the text_analysis function
def text_analysis(text: str, userId: int, postId: int, metadata: dict, doNotStore: bool = True) -> dict:
    """
    Analyzes text for inappropriate content.

    Args:
        text (str): The text content to be analyzed.
        userId (int): User ID of the user.
        postId (int): Post ID of the content.
        metadata (dict): Any extra information to be provided.
        doNotStore (bool): Whether to store the content. If set to True, the content won't enter the review queue.

    Returns:
        dict: The result of the text analysis.
    """
    conn = http.client.HTTPSConnection("moderationapi.com")

    payload = {
        "value": text,
        "doNotStore": doNotStore,
        "authorId": str(userId),
        "contextId": str(postId),
        "metadata": metadata
    }

    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": "Bearer proj_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2M2UxN2YzZDBlNWUwNzIwY2EwNjg3NSIsInVzZXJJZCI6IjY2M2UxNWEyNTRjYTE2NDNiOWRmZThkMSIsInRpbWVzdGFtcCI6MTcxNTM0NTM5NTU5NiwiaWF0IjoxNzE1MzQ1Mzk1fQ.PJlzguwYSbfjhtpLgwrkb9ZMgwUP0KARzQ3Y6-v2dpM",
        "Content-Type": "application/json"
    }

    conn.request("POST", "/api/v1/moderate/text", data, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return json.loads(data)

# Title of the application
st.title("Text Moderation App")

# Text input
text_content = st.text_area(label="Enter Text Content")

# Post ID input
post_id = st.text_input(label="Enter Post ID")

# User ID input
user_id = st.text_input(label="Enter User ID")

# A button to trigger the analysis
if st.button('Analyze Text'):
    # Validate input fields
    if not text_content or not post_id or not user_id:
        st.error("Please provide all required inputs: Text Content, Post ID, and User ID.")
    else:
        try:
            # Call the text analysis function
            res = text_analysis(text_content, int(user_id), int(post_id), {})

            # Display the results
            st.write("Inappropriate:", res.get('flagged', 'Unknown'))
            st.write(res)
        except Exception as e:
            st.error(f"An error occurred: {e}")
