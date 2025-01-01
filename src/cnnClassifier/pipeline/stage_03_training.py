from src.cnnClassifier.components.training import Training
import sys , os
from src.cnnClassifier import logger
from src.cnnClassifier.exception.exception import customexception
from src.cnnClassifier.config.configuration import ConfigurationManager


class TrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
    
    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()

            logger.info(' Training pipeline completed successfully.')
        except Exception as e:
            raise customexception(e, sys)
        
        