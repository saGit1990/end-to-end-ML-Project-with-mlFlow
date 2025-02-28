from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger

stage_name = "DATA INGESTION STAGE"

class DataIngestionPipeline:
    def __init__(self):
        pass 
    
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e: 
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {stage_name} started <<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>> stage {stage_name} completed <<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e