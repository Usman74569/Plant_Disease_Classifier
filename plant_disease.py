import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import json

# Load model and labels
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("plant_disease_model.keras")

@st.cache_resource
def load_class_labels():
    with open("class_labels.json", "r") as f:
        return json.load(f)

model = load_model()
class_labels = load_class_labels()
class_names = class_labels

# Set page config
st.set_page_config(page_title="🌿 Plant Disease Classifier", layout="centered")

st.title("🌿 Plant Disease Detection")
st.write("Upload a leaf image, and the model will predict the disease.")

# Upload image
uploaded_file = st.file_uploader("Choose a plant image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    img_resized = image.resize((128, 128)) ` # Change to your model's input shape
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)

    st.success(f"**Prediction:** {predicted_class}")
    st.info(f"**Confidence:** {confidence * 100:.2f}%")
