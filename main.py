import streamlit as st

st.set_page_config(page_title='Welcome to Multi-Mode Prediction App', layout="centered")
# st.title("Welcome to Multi-Mode Prediction App")

app_choice = st.selectbox("Select your app mode:", ["Standalone Mode", "FastAPI Client Mode"])

if app_choice == "Standalone Mode":
    import streamlit_standalone_app
    streamlit_standalone_app.main()  # Assuming you wrap your code in `def main():` there.

elif app_choice == "FastAPI Client Mode":
    import streamlit_app
    streamlit_app.main()  # Same here, wrap your streamlit_app.py code into `main()`.
