import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # change to DEBUG for more detail
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )