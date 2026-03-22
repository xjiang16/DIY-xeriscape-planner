# DIY-Xeriscape-Planner 🌵
A Python-based tool built with Streamlit to help homeowners visualize sustainable, drought-tolerant landscaping.

Built with **Streamlit** and **OpenCV/Pillow**, this tool bridges the gap between static gardening ideas and functional DIY planning.

### Current Features:
- **Photo Upload:** Support for JPG, PNG, and HEIC house exterior photos.
- **Interactive Canvas:** A custom-built drawing layer that allows users to mark plant placements directly on their yard photo.
- **Real-time Metrics:** Automatically counts and tracks the number of plants planned in the current session.
- **Sustainability Focus:** Specifically tailored for Xeriscaping (low-water) design principles.

## Tech Stack
- **Language:** Python 3.10+
- **Frontend/App Framework:** Streamlit
- **Image Processing:** Pillow (PIL)
- **Interactive Components:** Streamlit Drawable Canvas

## Roadmap
- [ ] **Phase 1:** Image Upload & Side-by-side Layout (Completed)
- [ ] **Phase 2:** Interactive Coordinate Mapping & Canvas (Current)
- [ ] **Phase 3:** Replace coordinate boxes with transparent SVG/PNG plant stickers.
- [ ] **Phase 4:** AI-powered "Grass Removal" using Segment Anything (SAM) to visualize gravel/mulch textures.

## Installation
1. Clone the repo: `git clone https://github.com/xjiang16/DIY-xeriscape-planner.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`