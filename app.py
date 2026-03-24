import streamlit as st
import io
from PIL import Image
from pillow_heif import register_heif_opener
from streamlit_drawable_canvas import st_canvas

register_heif_opener()

# --- SESSION STATE ---
# This acts as the "Memory" for which plant goes with which click
if "plant_history" not in st.session_state:
    st.session_state["plant_history"] = []

st.set_page_config(page_title="DIY Xeriscape Planner", layout="wide")
st.title("🌵DIY Xeriscape Planner🪏🪴")

# --- SIDEBAR ---
st.sidebar.header("User Uploads")
uploaded_pic = st.sidebar.file_uploader("Upload your yard photo", type=["jpg", "jpeg", "png", "HEIC"])
plant_choice = st.sidebar.selectbox("Select Plant to Place:", ["Agave", "Prickly Pear", "Mexican Grass"])
sticker_path = f"assets/{plant_choice.lower().replace(' ', '_')}.png"
tool_mode = st.sidebar.radio("Tool:", ("point", "transform"))

if st.sidebar.button("Reset Design"):
    st.session_state["plant_history"] = [] # Clear memory
    st.rerun()

# --- MAIN INTERFACE ---
if uploaded_pic is not None:
    image = Image.open(uploaded_pic)
    width, height = image.size
    display_width = 700
    display_height = int(height * (display_width / width))

    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Your Canvas")
        st.write(f"✨ **Currently Placing:** {plant_choice}")
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            background_image=image,
            update_streamlit=True,
            height=display_height,
            width=display_width,
            drawing_mode=tool_mode,
            point_display_radius=10,
            key="canvas",
        )

        # UPDATE MEMORY: Every time a new point is added, save the current plant choice
        if canvas_result.json_data is not None:
            objects = canvas_result.json_data["objects"]
            if len(objects) > len(st.session_state["plant_history"]):
                st.session_state["plant_history"].append(sticker_path)

    with col2:
        st.header("Design Summary")
        num_objects = len(canvas_result.json_data["objects"]) if canvas_result.json_data else 0
        st.metric("Total Plants Planned", num_objects)

        if st.button("Generate Final Design"):
            if num_objects > 0:
                st.write("Creating your multi-plant design...")
                final_design = image.copy().convert("RGBA")

                # We loop through the points and the memory list at the same time
                for i, obj in enumerate(canvas_result.json_data["objects"]):
                    try:
                        # Get the sticker path from our memory list
                        this_sticker_path = st.session_state["plant_history"][i]
                        sticker = Image.open(this_sticker_path).convert("RGBA")

                        # Resize
                        new_size = int(width * 0.1)
                        sticker = sticker.resize((new_size, new_size))

                        # Placement Math
                        x = int(obj["left"] * (width / display_width))
                        y = int(obj["top"] * (height / display_height))
                        s_w, s_h = sticker.size
                        final_design.paste(sticker, (x - s_w//2, y - s_h//2), sticker)
                    except Exception as e:
                        st.error(f"Error placing plant {i+1}: {e}")

                st.subheader("Your Finished Plan")
                st.image(final_design, use_column_width=True)

                # Download Logic
                buf = io.BytesIO()
                final_design.convert("RGB").save(buf, format="JPEG")
                st.download_button(label="💾 Download Plan", data=buf.getvalue(), file_name="my_plan.jpg")
            else:
                st.warning("Place some plants first!")

else:
    st.info("👆 Please upload a photo in the sidebar to get started.")