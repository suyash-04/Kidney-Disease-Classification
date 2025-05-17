import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        self.model_path = os.path.join("artifacts", "training", "model.h5")
        
        # Verify model file exists
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}")
        
        # Load model during initialization
        try:
            logger.info(f"Loading model from {self.model_path}")
            self.model = load_model(self.model_path)
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise
    
    def predict(self):
        try:
            # Load and preprocess image
            logger.info(f"Processing image: {self.filename}")
            test_image = image.load_img(self.filename, target_size=(299, 299))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            test_image = test_image/255.0
            
            # Make prediction
            logger.info("Making prediction")
            result = self.model.predict(test_image)
            predicted_class = np.argmax(result[0])
            logger.info(f"Prediction result: {result}")
            logger.info(f"Predicted class: {predicted_class}")
            
            # Return result
            prediction = 'Tumor Detected' if predicted_class == 1 else 'Normal'
            return [{"image": prediction}]
            
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            return [{"error": f"Prediction failed: {str(e)}"}]
        