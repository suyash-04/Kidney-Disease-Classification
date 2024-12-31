from src.cnnClassifier.components.data_ingestion import DataIngestion
import sys , os
from src.cnnClassifier import logger
from src.cnnClassifier.exception.exception import customexception
from src.cnnClassifier.config.configuration import ConfigurationManager

class DataIngestionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
    
    def main(self):
        try:
            config = self.config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config)
            data_ingestion.download_data()
            data_ingestion.extract_zip_file()
            logger.info('Data ingestion pipeline completed successfully.')
        except Exception as e:
            raise customexception(e, sys)
        
        