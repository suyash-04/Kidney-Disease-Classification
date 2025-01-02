import tensorflow as tf
from src.cnnClassifier.utils.utils import save_json
from src.cnnClassifier.exception.exception import customexception
from pathlib import Path
from src.cnnClassifier.entity.config_entity import EvaluationConfig


class Evaluation:
    def __init__(self, config : EvaluationConfig):
        self.config = config
    
    def _valid_generator(self):
        data_generator = dict(
            rescale = 1./255,
            validation_split = 0.2
        )
        
        data_flow = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = 'bilinear'
        )
        valid_datagenerator  = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator # type: ignore
        )
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory= self.config.training_path,
            subset = "validation",
            shuffle = True,
            **data_flow # type: ignore
        )
        
    @staticmethod
    def load_model(path : Path)->tf.keras.Model:
            return tf.keras.models.load_model(path) #type: ignore
        
    def evaluation(self):
            self.model = self.load_model(self.config.model_path)
            self._valid_generator()
            self.score = self.model.evaluate(self.valid_generator)
            
    def save_score(self):
            scores  = {"loss ": self.score[0], "accuracy" : self.score[1]}
            save_json(path = Path("scores.json"), data= scores)