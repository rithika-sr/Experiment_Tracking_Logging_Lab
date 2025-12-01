from app.logger_config import get_logger

logger = get_logger("heart_app.analyzer")

def analyze_numeric_columns(df):
    logger.info("Starting analysis on numeric columns...")

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        logger.error("No numeric columns found in dataset.")
        return None

    results = {}

    try:
        for col in numeric_df.columns:
            try:
                col_mean = numeric_df[col].mean()
                col_max = numeric_df[col].max()

                results[col] = {
                    "mean": col_mean,
                    "max": col_max
                }

                logger.debug(f"Analyzed column '{col}' -> mean={col_mean}, max={col_max}")

            except Exception:
                logger.error(f"Error analyzing column '{col}'", exc_info=True)

        logger.info("Analysis completed successfully.")
        return results

    except Exception:
        logger.error("Unexpected error during analysis.", exc_info=True)
        return None
