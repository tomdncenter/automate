from prefect import flow, task
from services.logger import configure_logging

logger = configure_logging("app.log")

@task
def do_job():
    logger.info("Running Script A")

@flow
def flow_test():
    do_job()

if __name__ == "__main__":
    flow_test()
