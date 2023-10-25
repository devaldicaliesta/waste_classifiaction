import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Streamlit configuration
st.set_page_config(page_title="Waste Classification App", page_icon="🗑️")

# Define your FastAPI API URL
api_url = "http://127.0.0.1:8000/predict"  # Replace with the correct URL

st.title("Waste Classification App")
st.write("This app is designed to predict waste types.")
st.write("The available classes are: 'Aluminium', 'Carton', 'Glass', 'Organic Waste', 'Other Plastics', 'Paper and Cardboard', 'Plastic', 'Textiles', 'Wood'")
st.write("Please note that the predictions may not always be accurate as the model may need further improvement.")

# Initialize the uploaded_image variable
uploaded_image = st.file_uploader("Upload an image for waste classification", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Process the uploaded image
    image_to_process = Image.open(uploaded_image)

    # Convert the image to bytes
    image_bytes = BytesIO()
    image_to_process.save(image_bytes, format='JPEG')

    # Make a request to the FastAPI API
    response = requests.post(api_url, files={"file": image_bytes.getvalue()})

    if response.status_code == 200:
        result = response.json()
        st.subheader("Prediction Results")
        st.write(f"Class: {result['class']}")
        st.write(f"Confidence: {result['confidence']:.2f}")
    else:
        st.error("Error making a prediction. Please try again.")
