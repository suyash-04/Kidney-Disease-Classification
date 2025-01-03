from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen= True)
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_data_file : Path
    unzip_dir : Path
    
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir : Path
    base_model_path : Path
    updated_base_model_path : Path
    params_image_size : list
    params_learning_rate : float
    params_include_top : bool
    params_weights : str
    params_classes : int

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path : Path
    updated_base_model_path : Path
    training_path : Path
    params_epochs : int
    params_image_size : list
    params_batch_size : int
    params_is_augmentation : bool

@dataclass(frozen=True)
class EvaluationConfig:
    model_path : Path
    training_path : Path
    params_image_size : list
    all_params : dict
    mlflow_uri : str
    params_batch_size : int
    