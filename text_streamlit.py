import streamlit as st
from text import text_analysis

st.title("Text Moderation")


text_content=st.text_area(label="Enter a text")

post_id=st.text_input(label="Enter Post Id")

user_id=st.text_input(label="Enter user Id")

activate_feature=st.checkbox("Send for human Review")

if st.button("Analyze text"):
    if not text_content or not post_id or not user_id:
        st.error("Please provide all required fields")

    else:
        try:
            doNotStore= not activate_feature
            res=text_analysis(text_content,post_id,user_id,{},doNotStore)

            st.write("Inappropriate: ", res['flagged'])
            st.write(res)

        except Exception as e:
            st.error(f"An error occurred : {e}")
