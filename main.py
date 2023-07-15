from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f">>>>>> STAGE \"{STAGE_NAME}\" STARTED <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> STAGE \"{STAGE_NAME}\" COMPLETED <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e