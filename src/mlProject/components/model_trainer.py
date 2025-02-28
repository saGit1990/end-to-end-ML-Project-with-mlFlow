import pandas as pd 
import os 
from mlProject import logger 
from sklearn.linear_model import ElasticNet
import joblib
from mlProject.config.configuration import ModelTrainerConfig


class ModelTrainerPipeline:
    def __init__(self, config = ModelTrainerConfig):
        self.config = config
        
    
    def train(self):
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)
        
        train_x = train_df.drop([self.config.target_column], axis = 1)
        test_x = test_df.drop([self.config.target_column], axis = 1)
        train_y = train_df[[self.config.target_column]]
        test_y = test_df[[self.config.target_column]]
        
        lr = ElasticNet(
            alpha= self.config.alpha,
            l1_ratio= self.config.l1_ratio,
            random_state=42
        )
        
        lr.fit(train_x, train_y)
        
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))