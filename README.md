# DIY-Xeriscape-Planner 🌵

An interactive web application built with Streamlit that allows homeowners to visualize drought-tolerant landscape designs by overlaying plant "stickers" onto photos of their own property.
Built with **Streamlit** and **OpenCV/Pillow**, this tool bridges the gap between static gardening ideas and functional DIY planning.

## 🚀 Key Features
- **Cross-Platform Image Support:** Fully compatible with HEIC (iPhone), PNG, and JPEG formats.
- **Interactive Design Canvas:** Precision placement of plants using a coordinate-mapped drawing interface.
- **Multi-Plant Memory:** Utilizes Streamlit Session State to track and remember different plant species selections across multiple clicks.
- **High-Resolution Rendering:** Scales UI coordinates to original image dimensions for a professional-grade final export.
- **Instant Budgeting:** Real-time plant counting for project estimation.
- **Export Capabilities:** Generate and download finalized high-resolution JPEG designs.

## Tech Stack
- **Language:** Python 3.10+
- **Frontend/App Framework:** Streamlit
- **Image Processing:** Pillow (PIL)
- **Interactive Components:** Streamlit Drawable Canvas
- **Data Handling:** JSON coordinate mapping & Python Session State

## 📈 Roadmap
- [x] Phase 1: Layout & Image Upload
- [x] Phase 2: Interactive Canvas Integration
- [x] Phase 3: Coordinate Scaling & Multi-Plant Rendering Logic
- [ ] Phase 4: Dynamic Cost Estimation & Plant Database
- [ ] Phase 5: AI-Powered "Green-to-Gravel" Ground Cover Replacement

## Installation
1. Clone the repo: `git clone https://github.com/xjiang16/DIY-xeriscape-planner.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`