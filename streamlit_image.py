import streamlit as st
from image import image_analysis
st.title("Image Moderation App")



# st.file_uploader("Upload your image here", type=['png','jpg'], accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
img_url=st.text_input(label="Enter Image URL")

if img_url:
    st.markdown(f"![Alt Text]({img_url})")

post_id = st.text_input(label="Enter Post ID")
user_id = st.text_input(label="Enter User ID")

activate_feature=st.checkbox("Send for human Review")

if st.button('Analyze Image'):
    if not img_url or not post_id or not user_id:
        st.error("provide all required inputs : like img_url, post_id,user_id")
    
    else:
        try:
            doNotStore= not activate_feature
            res=image_analysis(img_url,post_id,user_id,{},doNotStore)

            #results
            st.write("Inappropriate: ",res['flagged'])
            st.write(res)

        except Exception as e:
            st.error(f"an erroe occurred:{e}")






