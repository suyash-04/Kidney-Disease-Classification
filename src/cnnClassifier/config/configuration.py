import os, sys
from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.utils import read_yaml , create_direcories
from src.cnnClassifier.exception.exception import customexception
from src.cnnClassifier.entity.config_entity import DataIngestionConfig , PrepareBaseModelConfig

class ConfigurationManager():
    def __init__(self, CONFIG_FILE_PATH =CONFIG_FILE_PATH , PARAMS_FILE_PATH = PARAMS_FILE_PATH):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)
        create_direcories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config  = self.config.data_ingestion
            
            create_direcories([config.root_dir])
            data_ingestion_config = DataIngestionConfig(
                root_dir = Path(config.root_dir),
                source_url = config.source_url,
                local_data_file = Path(config.local_data_file),
                unzip_dir = Path(config.unzip_dir)
            )
            return data_ingestion_config
        except Exception as e:
            raise customexception(e, sys)
    def get_prepare_base_model_config(self)->PrepareBaseModelConfig:
        try:    
            config = self.config.prepare_base_model
            params = self.params
            create_direcories([config.root_dir])
            prepare_base_model_config = PrepareBaseModelConfig(
                root_dir = config.root_dir,
                base_model_path = config.base_model_path,
                updated_base_model_path = config.updated_base_model_path,
                params_image_size = params.IMAGE_SIZE,
                params_learning_rate = params.LEARNING_RATE,
                params_include_top = params.INCLUDE_TOP,
                params_weights = params.WEIGHTS,
                params_classes = params.CLASSES,
            )
            return prepare_base_model_config
        except Exception as e:
            raise customexception(e, sys)