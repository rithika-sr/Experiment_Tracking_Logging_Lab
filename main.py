from app.logger_config import get_logger
from app.data_loader import load_csv
from app.analyzer import analyze_numeric_columns

def main():
    logger = get_logger("heart_app.main")

    logger.info("Application started.")

    # Load dataset
    df = load_csv("heart.csv")

    if df is None:
        logger.error("Dataset failed to load. Stopping application.")
        return

    # Run analysis
    results = analyze_numeric_columns(df)

    if results is None:
        logger.error("Analysis failed. No results to display.")
        return

    # Print results to terminal nicely
    logger.info("Final Results:\n")
    for col, stats in results.items():
        print(f"{col} -> mean: {stats['mean']:.3f}, max: {stats['max']:.3f}")

    logger.info("Application finished successfully.")

if __name__ == "__main__":
    main()
