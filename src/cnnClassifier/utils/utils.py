import os ,sys
import yaml
from src.cnnClassifier import logger
from src.cnnClassifier.exception.exception import customexception
import json ,joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} read successfully")
            return ConfigBox(content)
    except Exception as e:
        raise customexception(e, sys)

@ensure_annotations
def create_direcories(path_to_direcories : list , verbose = True):
   try:
       for path in path_to_direcories:
            os.makedirs(path,exist_ok = True)
            if verbose:
                logger.info(f"directory : {path} created successfully")
            
   except Exception as e:
        raise customexception(e, sys)
    
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try:
        with open(path) as f:
            content = json.load(f)

        logger.info(f"json file loaded succesfully from: {path}")
        return ConfigBox(content)
    except Exception as e:
        raise customexception(e, sys)
    
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")