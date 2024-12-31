from src.cnnClassifier.components.prepare_base_model import PrepareBaseModel
import sys , os
from src.cnnClassifier import logger
from src.cnnClassifier.exception.exception import customexception
from src.cnnClassifier.config.configuration import ConfigurationManager


class PrepareBaseModelPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
    
    def main(self):
        try:
            config_manager = ConfigurationManager()
            prepare_base_model_config = config_manager.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.get_full_model()
            
            logger.info('Prepare Base Model pipeline completed successfully.')
        except Exception as e:
            raise customexception(e, sys)
        
        