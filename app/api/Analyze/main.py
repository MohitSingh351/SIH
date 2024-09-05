import sys
import tensorflow as tf
import cv2
import numpy as np

# Load your model
model = tf.keras.models.load_model('plant_disease_model.h5')

# Define the class labels as per your dataset
class_labels = [
    'Apple Apple_scab',
    'Apple Black_rot',
    'Apple Cedar_apple_rust',
    'Apple healthy',
    'Blueberry healthy',
    'Cherry_(including_sour) Powdery_mildew',
    'Cherry_(including_sour) healthy',
    'Corn_(maize) Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize) Common_rust_',
    'Corn_(maize) Northern_Leaf_Blight',
    'Corn_(maize) healthy',
    'Grape Black_rot',
    'Grape Esca_(Black_Measles)',
    'Grape Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape healthy',
    'Orange Haunglongbing_(Citrus_greening)',
    'Peach Bacterial_spot',
    'Peach healthy',
    'Pepper,_bell Bacterial_spot',
    'Pepper,_bell healthy',
    'Potato Early_blight',
    'Potato Late_blight',
    'Potato healthy',
    'Raspberry healthy',
    'Soybean healthy',
    'Squash Powdery_mildew',
    'Strawberry Leaf_scorch',
    'Strawberry healthy',
    'Tomato Bacterial_spot',
    'Tomato Early_blight',
    'Tomato Late_blight',
    'Tomato Leaf_mold',
    'Tomato Septoria_leaf_spot',
    'Tomato Spider_mites Two-spotted_spider_mite',
    'Tomato Target_spot',
    'Tomato Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato Tomato_mosaic_virus',
    'Tomato healthy'
]

# Define detailed information for each class
class_info = {
    'Apple Apple_scab': {
        'plant_name': 'Apple',
        'status': 'Apple scab',
        'cure': 'Apply fungicides like captan or sulfur.',
        'maintain_healthy': 'Regularly prune the tree and remove fallen leaves to improve air circulation.',
        'medicine': 'Captan, sulfur-based fungicides.'
    },
    'Apple Black_rot': {
        'plant_name': 'Apple',
        'status': 'Black rot',
        'cure': 'Apply fungicides like copper or sulfur.',
        'maintain_healthy': 'Ensure proper air circulation, prune infected branches, and remove fallen fruit.',
        'medicine': 'Copper fungicides, sulfur-based treatments.'
    },
    'Apple Cedar_apple_rust': {
        'plant_name': 'Apple',
        'status': 'Cedar apple rust',
        'cure': 'Apply fungicides like captan or sulfur.',
        'maintain_healthy': 'Remove nearby cedar trees or use resistant apple varieties; ensure proper air circulation.',
        'medicine': 'Captan, sulfur-based fungicides.'
    },
    'Apple healthy': {
        'plant_name': 'Apple',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering, balanced fertilization, and pruning to maintain air circulation.',
        'medicine': 'None'
    },
    'Blueberry healthy': {
        'plant_name': 'Blueberry',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering, proper soil pH maintenance, and mulching.',
        'medicine': 'None'
    },
    'Cherry_(including_sour) Powdery_mildew': {
        'plant_name': 'Cherry',
        'status': 'Powdery mildew',
        'cure': 'Apply fungicides like sulfur or potassium bicarbonate.',
        'maintain_healthy': 'Ensure proper air circulation and avoid overhead watering.',
        'medicine': 'Sulfur-based fungicides, potassium bicarbonate.'
    },
    'Cherry_(including_sour) healthy': {
        'plant_name': 'Cherry',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering, balanced fertilization, and pruning.',
        'medicine': 'None'
    },
    'Corn_(maize) Cercospora_leaf_spot Gray_leaf_spot': {
        'plant_name': 'Corn',
        'status': 'Gray leaf spot',
        'cure': 'Apply fungicides like azoxystrobin or chlorothalonil.',
        'maintain_healthy': 'Practice crop rotation and remove infected debris.',
        'medicine': 'Azoxystrobin, chlorothalonil.'
    },
    'Corn_(maize) Common_rust_': {
        'plant_name': 'Corn',
        'status': 'Common rust',
        'cure': 'Apply fungicides like azoxystrobin or myclobutanil.',
        'maintain_healthy': 'Plant rust-resistant varieties and ensure proper field sanitation.',
        'medicine': 'Azoxystrobin, myclobutanil.'
    },
    'Corn_(maize) Northern_Leaf_Blight': {
        'plant_name': 'Corn',
        'status': 'Northern Leaf Blight',
        'cure': 'Apply fungicides like propiconazole or tebubiconazole.',
        'maintain_healthy': 'Practice crop rotation and remove infected plant debris.',
        'medicine': 'Propiconazole, tebubiconazole.'
    },
    'Corn_(maize) healthy': {
        'plant_name': 'Corn',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering, fertilization, and proper crop management.',
        'medicine': 'None'
    },
    'Grape Black_rot': {
        'plant_name': 'Grape',
        'status': 'Black rot',
        'cure': 'Apply fungicides like mancozeb or copper.',
        'maintain_healthy': 'Ensure proper air circulation and prune affected vines.',
        'medicine': 'Mancozeb, copper-based fungicides.'
    },
    'Grape Esca_(Black_Measles)': {
        'plant_name': 'Grape',
        'status': 'Esca (Black Measles)',
        'cure': 'Apply fungicides like copper or sulfur.',
        'maintain_healthy': 'Ensure good vineyard management and avoid excessive irrigation.',
        'medicine': 'Copper fungicides, sulfur-based treatments.'
    },
    'Grape Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'plant_name': 'Grape',
        'status': 'Leaf blight',
        'cure': 'Apply fungicides like copper or sulfur.',
        'maintain_healthy': 'Improve air circulation around vines and avoid overhead watering.',
        'medicine': 'Copper fungicides, sulfur-based treatments.'
    },
    'Grape healthy': {
        'plant_name': 'Grape',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering, proper vine management, and pruning.',
        'medicine': 'None'
    },
    'Orange Haunglongbing_(Citrus_greening)': {
        'plant_name': 'Orange',
        'status': 'Huanglongbing (Citrus greening)',
        'cure': 'No known cure; remove infected trees.',
        'maintain_healthy': 'Plant disease-free trees and manage vector populations.',
        'medicine': 'None'
    },
    'Peach Bacterial_spot': {
        'plant_name': 'Peach',
        'status': 'Bacterial spot',
        'cure': 'Apply copper-based fungicides or antibiotics.',
        'maintain_healthy': 'Prune infected branches and ensure proper air circulation.',
        'medicine': 'Copper fungicides, antibiotics.'
    },
    'Peach healthy': {
        'plant_name': 'Peach',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering and proper fertilization.',
        'medicine': 'None'
    },
    'Pepper,_bell Bacterial_spot': {
        'plant_name': 'Pepper, bell',
        'status': 'Bacterial spot',
        'cure': 'Apply copper-based bactericides.',
        'maintain_healthy': 'Ensure good air circulation and avoid overhead watering.',
        'medicine': 'Copper-based bactericides.'
    },
    'Pepper,_bell healthy': {
        'plant_name': 'Pepper, bell',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering and proper fertilization.',
        'medicine': 'None'
    },
    'Potato Early_blight': {
        'plant_name': 'Potato',
        'status': 'Early blight',
        'cure': 'Apply fungicides like chlorothalonil or mancozeb.',
        'maintain_healthy': 'Practice crop rotation and avoid overhead watering.',
        'medicine': 'Chlorothalonil, mancozeb.'
    },
    'Potato Late_blight': {
        'plant_name': 'Potato',
        'status': 'Late blight',
        'cure': 'Apply fungicides like chlorothalonil or copper.',
        'maintain_healthy': 'Practice crop rotation and remove infected debris.',
        'medicine': 'Chlorothalonil, copper-based fungicides.'
    },
    'Potato healthy': {
        'plant_name': 'Potato',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering and proper fertilization.',
        'medicine': 'None'
    },
    'Raspberry healthy': {
        'plant_name': 'Raspberry',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering and proper fertilization.',
        'medicine': 'None'
    },
    'Soybean healthy': {
        'plant_name': 'Soybean',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering and proper fertilization.',
        'medicine': 'None'
    },
    'Squash Powdery_mildew': {
        'plant_name': 'Squash',
        'status': 'Powdery mildew',
        'cure': 'Apply fungicides like sulfur or potassium bicarbonate.',
        'maintain_healthy': 'Ensure proper air circulation and avoid overhead watering.',
        'medicine': 'Sulfur-based fungicides, potassium bicarbonate.'
    },
    'Strawberry Leaf_scorch': {
        'plant_name': 'Strawberry',
        'status': 'Leaf scorch',
        'cure': 'Apply fungicides like copper or chlorothalonil.',
        'maintain_healthy': 'Ensure proper air circulation and avoid overhead watering.',
        'medicine': 'Copper fungicides, chlorothalonil.'
    },
    'Strawberry healthy': {
        'plant_name': 'Strawberry',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering and proper fertilization.',
        'medicine': 'None'
    },
    'Tomato Bacterial_spot': {
        'plant_name': 'Tomato',
        'status': 'Bacterial spot',
        'cure': 'Apply copper-based bactericides.',
        'maintain_healthy': 'Ensure proper air circulation and avoid overhead watering.',
        'medicine': 'Copper-based bactericides.'
    },
    'Tomato Early_blight': {
        'plant_name': 'Tomato',
        'status': 'Early blight',
        'cure': 'Apply fungicides like chlorothalonil or mancozeb.',
        'maintain_healthy': 'Practice crop rotation and remove infected debris.',
        'medicine': 'Chlorothalonil, mancozeb.'
    },
    'Tomato Late_blight': {
        'plant_name': 'Tomato',
        'status': 'Late blight',
        'cure': 'Apply fungicides like chlorothalonil or copper.',
        'maintain_healthy': 'Practice crop rotation and remove infected debris.',
        'medicine': 'Chlorothalonil, copper-based fungicides.'
    },
    'Tomato Leaf_mold': {
        'plant_name': 'Tomato',
        'status': 'Leaf mold',
        'cure': 'Apply fungicides like copper or potassium bicarbonate.',
        'maintain_healthy': 'Ensure proper air circulation and avoid overhead watering.',
        'medicine': 'Copper fungicides, potassium bicarbonate.'
    },
    'Tomato Septoria_leaf_spot': {
        'plant_name': 'Tomato',
        'status': 'Septoria leaf spot',
        'cure': 'Apply fungicides like chlorothalonil or copper.',
        'maintain_healthy': 'Practice crop rotation and remove infected debris.',
        'medicine': 'Chlorothalonil, copper-based fungicides.'
    },
    'Tomato Spider_mites Two-spotted_spider_mite': {
        'plant_name': 'Tomato',
        'status': 'Two-spotted spider mite',
        'cure': 'Apply miticides or insecticidal soaps.',
        'maintain_healthy': 'Ensure proper air circulation and avoid overhead watering.',
        'medicine': 'Miticides, insecticidal soaps.'
    },
    'Tomato Target_spot': {
        'plant_name': 'Tomato',
        'status': 'Target spot',
        'cure': 'Apply fungicides like chlorothalonil or mancozeb.',
        'maintain_healthy': 'Practice crop rotation and remove infected debris.',
        'medicine': 'Chlorothalonil, mancozeb.'
    },
    'Tomato Tomato_Yellow_Leaf_Curl_Virus': {
        'plant_name': 'Tomato',
        'status': 'Tomato Yellow Leaf Curl Virus',
        'cure': 'No known cure; remove infected plants.',
        'maintain_healthy': 'Use virus-free seeds and control whiteflies.',
        'medicine': 'None'
    },
    'Tomato Tomato_mosaic_virus': {
        'plant_name': 'Tomato',
        'status': 'Tomato mosaic virus',
        'cure': 'No known cure; remove infected plants.',
        'maintain_healthy': 'Use virus-free seeds and control aphids.',
        'medicine': 'None'
    },
    'Tomato healthy': {
        'plant_name': 'Tomato',
        'status': 'Healthy',
        'cure': 'No action needed.',
        'maintain_healthy': 'Regular watering and proper fertilization.',
        'medicine': 'None'
    }
}

# Load and preprocess the image
image_path = 'tomato___yellow_leaf_curl.png'  # Path to the image file
image = cv2.imread(image_path)  # Read the image from the file
image = cv2.resize(image, (224, 224))  # Resize the image to match the input size of the model (224x224 pixels)
image = image.astype('float32') / 255.0  # Normalize the image pixel values to the range [0, 1]
image = np.expand_dims(image, axis=0)  # Add a batch dimension to the image array (required by the model)

# Predict the class of the image
predictions = model.predict(image)  # Use the model to predict the class probabilities for the image
predicted_class_index = np.argmax(predictions)  # Get the index of the class with the highest probability
predicted_class_label = class_labels[predicted_class_index]  # Map the index to the corresponding class label

# Retrieve detailed information
plant_info = class_info.get(predicted_class_label, None)  # Retrieve detailed information for the predicted class

if plant_info:  # Check if information for the predicted class is available
    print(f"Plant Name: {plant_info['plant_name']}")  # Print the plant name
    print(f"Status: {plant_info['status']}")  # Print the disease or status
    print(f"Cure: {plant_info['cure']}")  # Print the recommended cure
    print(f"Maintain Healthy: {plant_info['maintain_healthy']}")  # Print tips to maintain healthy plants
    print(f"Recommended Medicine: {plant_info['medicine']}")  # Print the recommended medicine
else:
    print("Information for this class is not available.")  # Inform the user if no information is available for the predicted class

