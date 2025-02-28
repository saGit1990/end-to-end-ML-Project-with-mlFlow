from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger

stage_name = "DATA VALIDATION STAGE"

class DataValidationPipeline:
    def __init__(self):
        pass 
    
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e: 
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {stage_name} started <<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>> stage {stage_name} completed <<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e