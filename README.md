
# 🌿 Plant Disease Classifier using CNN

This project is a deep learning-based classifier that detects plant diseases from leaf images. It includes model training, saving the trained model and label file, and a script (likely used in Streamlit) for prediction.

---

## 📁 Project Structure

```

Plant\_Disease\_Classifier/
├── Plant\_Disease\_Classifier/
│   ├── Plant\_disease\_prediction\_using\_CNN.ipynb   # Model training notebook
│   ├── class labels.json                          # Label names file
│   ├── plant\_disease.py                           # Prediction or Streamlit script
│   ├── plant\_disease\_model.keras                  # Saved Keras model
│   ├── requirements.txt                           # Required packages
├── test\_images/                                   # Folder of sample test images
├── README.md                                      # Project overview (this file)

````

---

## 🔧 How the Code Works

### 1. Training the Model (`Plant_disease_prediction_using_CNN.ipynb`)
- This notebook is used to:
  - Load and preprocess the dataset directly imported from Kaggle
  - Build and train a CNN model
  - Save the trained model to `plant_disease_model.keras`
  - Save the label map to `class labels.json`

### 2. Prediction (`plant_disease.py`)
- This script:
  - Loads the saved `.keras` model and `class labels.json`
  - Accepts input image
  - Preprocesses and predicts the plant disease
  - Can be used in a web app (e.g., Streamlit)

---

## ▶️ How to Use

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Plant_Disease_Classifier.git
cd Plant_Disease_Classifier
````

### Step 2: Install Dependencies

```bash
pip install -r Plant_Disease_Classifier/requirements.txt
```

### Step 3: (Optional) Retrain the Model

* Open the notebook `Plant_disease_prediction_using_CNN.ipynb`
* Train and export the model and labels

### Step 4: Run the Prediction Script or App

* If using Streamlit:

```bash
streamlit run Plant_Disease_Classifier/plant_disease.py
```

* If it’s a CLI script:

```bash
python Plant_Disease_Classifier/plant_disease.py
```

---

## 📦 Requirements

Main dependencies (see full list in `requirements.txt`):

* Python 3.x
* TensorFlow / Keras
* NumPy
* Streamlit (if using as a web app)
* Pillow

---

## 📁 test\_images

This folder contains sample leaf images for testing the prediction script or Streamlit app.

---

## 🧠 Model Info

* Type: CNN (Convolutional Neural Network)
* Framework: Keras
* Output: Plant disease prediction
* Saved as: `plant_disease_model.keras`

---

## 🙋‍♂️ Author

Usman Syed
Civil Engineering Student
Exploring AI for real-world applications 🌿

---

## 📌 Notes

* Keep model file and label file in the same directory as your app script.
* You can retrain the model anytime using the notebook.
* Consider deploying your Streamlit app on Streamlit Cloud or Hugging Face Spaces.

```
