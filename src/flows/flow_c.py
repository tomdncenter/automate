from prefect import flow, task

@task
def do_job():
    print("Running Script C")

@flow
def flow_c():
    do_job()

if __name__ == "__main__":
    flow_c()
