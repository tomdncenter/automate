import logging

# Configure logging
def configure_logging(name: str) -> logging.Logger:
    logging.basicConfig(
        filename=name,          # log file name
        filemode="a",                # "a" = append, "w" = overwrite
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO           # log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    )
    return logging.getLogger()