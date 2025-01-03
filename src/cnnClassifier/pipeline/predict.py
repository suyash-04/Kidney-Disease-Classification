import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (299,299))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        test_image = test_image/255.0
        result = (model.predict(test_image))
        print(result)
        predicted_class = np.argmax(result[0])
        print(predicted_class)
        if predicted_class == 1:
            prediction = 'Tumor Detected'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]
        