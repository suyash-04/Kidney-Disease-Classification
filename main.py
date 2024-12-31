from src.cnnClassifier.exception.exception import customexception
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.cnnClassifier import logger
import sys

STAGE_NAME = "DATA INGESTION"

try :
    print(f">>>>>>>>>{STAGE_NAME}<<<<<<<<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>{STAGE_NAME}  completed<<<<<<<<<<<<")

except Exception as e:
    raise customexception(e, sys)
    
    
STAGE_NAME = "PREPARE BASE MODEL"       
try :
    print(f">>>>>>>>>{STAGE_NAME}<<<<<<<<<<<<<<<")
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>{STAGE_NAME}  completed<<<<<<<<<<<<")

except Exception as e:
    raise customexception(e, sys)
    