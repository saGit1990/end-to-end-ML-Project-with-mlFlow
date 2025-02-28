import os 
import pandas as pd
from mlProject import logger
from mlProject.config.configuration import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config 
        
    def validate_all_columns(self) -> bool:
        try:
            validation_state = None 
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            
            all_schema = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_state = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'validation status: {validation_state}')
                else:
                    validation_state = True 
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'validation status: {validation_state}')
                        
            return validation_state
        except Exception as e:
            logger.exception(e)
            raise e