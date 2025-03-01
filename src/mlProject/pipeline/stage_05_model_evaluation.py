from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

stage_name = "MODEL EVALUATION STAGE"

class ModelEvaluationPipeline:
    def __init__(self):
        pass 
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_eval_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_eval_config)
            model_evaluation.log_into_mlflow()
        except Exception as e: 
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {stage_name} started <<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>> stage {stage_name} completed <<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e