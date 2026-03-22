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

    width, height = image.size

    # Scale down for display if it's a huge photo
    display_width = 700
    display_height = int(height * (display_width / width))

    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Your Canvas")
        st.write("✨ **Action:** Click and drag on the photo to mark where you want plants!")
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=2,
            stroke_color="#FFFFFF",
            bg_image=image,
            update_streamlit=True,
            height=display_height,
            width=display_width,
            drawing_mode="rect",
            key="canvas",
        )

    with col2:
        st.header("Design Summary")

        # This part reads the "Drawing" and counts the boxes
        if canvas_result.json_data is not None:
            num_objects = len(canvas_result.json_data["objects"])
            st.metric("Total Plants Planned", num_objects)

        st.text_area("Design Notes", placeholder="e.g., Use Mexican Feather Grass in the back...")

        if st.button("Save Design Progress"):
            st.success("Work tracked! (Next: We'll link this to a database)")

        if st.sidebar.button("Reset Design"):
            st.rerun()

else:
    st.info("👆 Please upload a photo in the sidebar to get started.")