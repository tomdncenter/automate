from prefect import flow, task
from src.services.logger import configure_logging


@task
def do_job():
    logger = configure_logging("app.log")
    logger.info("Running Script A")

@flow
def flow_test():
    do_job()

if __name__ == "__main__":
    flow_test()
