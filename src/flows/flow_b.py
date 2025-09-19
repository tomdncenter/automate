from prefect import flow, task

@task
def do_job():
    print("Running Script B")

@flow
def flow_b():
    do_job()

if __name__ == "__main__":
    flow_b()
