from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os
import uuid

app = Flask(__name__)

# Load the pre-trained model
model = load_model('model/pneumonia_model.h5')

def prepare_image(image_path):
    img = load_img(image_path, target_size=(150, 150))  # Adjust target_size based on your model
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize the image
    return img_array

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'success': False})
    
    if file:
        filename = f"{uuid.uuid4()}.jpg"  # Generate a unique name for the file
        filepath = os.path.join('uploads', filename)
        file.save(filepath)
        
        # Prepare the image and make prediction
        img = prepare_image(filepath)
        prediction = model.predict(img)
        
        # Assuming the model has a binary output (Pneumonia or Normal)
        result = 'Pneumonia Detected' if prediction[0][0] > 0.5 else 'Normal'
        
        return jsonify({'success': True, 'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
