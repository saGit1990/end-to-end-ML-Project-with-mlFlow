from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger

stage_name = "DATA TRANSFORMATION STAGE"

class DataTransformationPipeline:
    def __init__(self):
        pass 
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_splitting()
        except Exception as e: 
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {stage_name} started <<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>> stage {stage_name} completed <<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e