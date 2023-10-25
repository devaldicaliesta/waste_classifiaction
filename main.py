import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Streamlit configuration
st.set_page_config(page_title="Waste Classification App", page_icon="🗑️")

# Define your FastAPI API URL
api_url = "http://localhost:8000/predict/"  # Replace with the correct URL

st.title("Waste Classification App")
st.write("This app is designed to predict waste types.")
st.write("The available classes are: 'Aluminium', 'Carton', 'Glass', 'Organic Waste', 'Other Plastics', 'Paper and Cardboard', 'Plastic', 'Textiles', 'Wood'")
st.write("Please note that the predictions may not always be accurate as the model may need further improvement.")

# Initialize the captured_image variable
captured_image = None

# Choose whether to capture or upload an image
option = st.radio("Select an image source:", ("Capture Image", "Upload Image"))

if option == "Capture Image":
    # Capture an image through Streamlit camera
    st.write("Click the button below to capture an image for waste classification:")
    if st.button("Capture Image"):
        captured_image = st.camera()

        if captured_image is not None:
            image = Image.fromarray(captured_image)
            st.image(image, caption="Captured Image", use_column_width=True)
else:
    # Upload image through Streamlit
    uploaded_image = st.file_uploader("Upload an image for waste classification", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    # Process the selected image
    if uploaded_image is not None or captured_image is not None:
        if uploaded_image is not None:
            image_to_process = Image.open(uploaded_image)
        else:
            image_to_process = Image.fromarray(captured_image)

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