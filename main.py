from fastapi import FastAPI

application = FastAPI()

@application.get("/transaction")
def get_transaction():
    return "balikan"
