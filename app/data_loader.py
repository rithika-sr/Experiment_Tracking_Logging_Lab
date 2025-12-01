import pandas as pd
from app.logger_config import get_logger

logger = get_logger("heart_app.data_loader")

def load_csv(path: str):
    logger.info(f"Attempting to load dataset from: {path}")

    try:
        df = pd.read_csv(path)
        logger.debug(f"Dataset loaded successfully with shape: {df.shape}")
        logger.debug(f"Columns found: {list(df.columns)}")
        return df

    except FileNotFoundError:
        logger.error("File not found. Please check the path.", exc_info=True)

    except pd.errors.EmptyDataError:
        logger.error("The file is empty.", exc_info=True)

    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}", exc_info=True)
