import os
import numpy as np
import io
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Flask app config
app = Flask(__name__, template_folder='templates', static_folder='static')

# Load pre-trained model
model = load_model("model1.keras")

# Define class labels
categories = ['glioma', 'meningioma', 'pituitary', 'notumor']

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    img = load_img(io.BytesIO(image.read()), target_size=(128, 128))
    img = img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    predicted_label = np.argmax(prediction)
    label_name = categories[predicted_label]
    print("Raw prediction:", prediction)
    return jsonify({'prediction': label_name})

# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=5001)
