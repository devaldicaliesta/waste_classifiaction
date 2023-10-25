import io
import uvicorn
import numpy as np
from fastapi import FastAPI, UploadFile
from PIL import Image
import tensorflow as tf

app = FastAPI(
    title="Waste Classification Model API",
    description="A simple API that uses an Inception model to predict waste types",
    version="0.1",
)

# Load the InceptionV3 model
model =  tf.keras.models.load_model("inceptionv3_model.h5")

# Define the class labels
class_labels = ['Aluminium', 'Carton', 'Glass', 'Organic Waste', 'Other Plastics', 'Paper and Cardboard', 'Plastic', 'Textiles', 'Wood']

@app.post("/predict/")
async def predict(file: UploadFile):
    try:
        # Read and preprocess the image
        image = Image.open(io.BytesIO(file.file.read()))
        image = image.resize((256, 256))
        img_array = tf.keras.preprocessing.image.img_to_array(image)
        img_array = tf.expand_dims(img_array, 0)

        # Make predictions using the model
        predictions = model.predict(img_array)
        predicted_class = class_labels[np.argmax(predictions)]

        return {"class": predicted_class, "confidence": float(predictions.max())}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Waste Classification Model API. Use the /predict/ endpoint to make predictions."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)