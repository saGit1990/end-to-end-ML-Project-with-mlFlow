from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainerPipeline
from mlProject import logger

stage_name = "MODEL TRAINING STAGE"

class ModelTrainingPipeline:
    def __init__(self):
        pass 
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_training_config = config.get_model_trainer_config()
            model_trainer = ModelTrainerPipeline(config=model_training_config)
            model_trainer.train()
        except Exception as e: 
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {stage_name} started <<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {stage_name} completed <<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e