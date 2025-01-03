from src.cnnClassifier.components.model_evaluation import Evaluation
import sys , os
from src.cnnClassifier import logger
from src.cnnClassifier.exception.exception import customexception
from src.cnnClassifier.config.configuration import ConfigurationManager


class EvaluationPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
    
    def main(self):
        try:
            config = ConfigurationManager()
            evaluation_config = config.get_evaluation_config()
            evaluation = Evaluation(evaluation_config)
            evaluation._valid_generator()
            evaluation.evaluation()
            evaluation.save_score()
            evaluation.log_into_mlflow()

        except Exception as e:
            raise customexception(e, sys)
    
