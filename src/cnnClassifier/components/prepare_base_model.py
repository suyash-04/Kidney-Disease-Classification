import os , sys
import tensorflow as tf
from pathlib import Path
from src.cnnClassifier import logger
from src.cnnClassifier.exception.exception import customexception
from src.cnnClassifier.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
        
    def get_base_model(self):
        self.model = tf.keras.applications.InceptionV3(
            input_shape= tuple(self.config.params_image_size),
            weights = self.config.params_weights,
            include_top= self.config.params_include_top
        )
        self.save_model(model = self.model , path = self.config.base_model_path)
        
    
    def prepare_full_model(self, model , classes , freeze_all , freeze_till , learning_rate):
        try:
            if freeze_all:
                for layer in model.layers:
                    layer.trainable = False
            else:
                for layer in model.layers[:freeze_till]:
                    layer.trainable = False
                for layer in model.layers[freeze_till:]:
                    layer.trainable = True
            x = model.output
            
            x = tf.keras.layers.Dense(1024, activation='relu')(x)
            x = tf.keras.layers.Dense(512, activation='relu')(x)
            x = tf.keras.layers.Dense(256, activation='relu')(x)
            x = tf.keras.layers.Dense(128, activation='relu')(x)
            
            output = tf.keras.layers.Dense(units = classes, activation='softmax')(x)
            full_model = tf.keras.models.Model(
                inputs = model.input,
                outputs = output,
                )
            full_model.compile(
                optimizer=tf.keras.optimizers.Adam(lr=learning_rate),
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=['accuracy']
            )
            full_model.summary()
            return full_model
            
        except Exception as e:
            raise customexception(e, sys)
    
    def get_full_model(self):
        self.full_model = self.prepare_full_model(
            model = self.model,
            classes = self.config.params_classes,
            freeze_all = True,
            freeze_till = None,
            learning_rate = self.config.params_learning_rate
        )
        self.save_model(model = self.full_model, path = self.config.updated_base_model_path)
                        
    @staticmethod
    def save_model(model : tf.keras.Model, path : Path):
        model.save(path)