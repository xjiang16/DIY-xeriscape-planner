import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="DIY Xeriscape Planner", layout="wide")
st.title("🌵DIY Xeriscape Planner🪏🪴")
st.markdown("""
Welcome to the DIY Xeriscape Planner 🌵Upload a photo of your front or backyard to start planning your 
**drought-tolerant** landscape.
""")

# --- SIDEBAR ---
st.sidebar.header("User Uploads")
uploaded_pic = st.sidebar.file_uploader("Upload your yard photo", type=["jpg", "jpeg", "png", "HEIC"])

# --- MAIN INTERFACE ---
if uploaded_pic is not None:
    image = Image.open(uploaded_pic)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Your Canvas")
        st.image(image, use_container_width=True)

    with col2:
        st.header("Design Tools")
        add_agave = st.checkbox("Add Agave Americana")
        add_rocks = st.checkbox("Add River Rocks")

        if add_agave:
            st.info("📍 Imagine an Agave sticker appearing on the photo!")
        st.text_area("Design Notes", placeholder="e.g., Replace grass with decomposed granite...")

else:
    st.info("👆 Please upload a photo in the sidebar to get started.")