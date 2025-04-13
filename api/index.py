from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/transaction")
def get_transaction():
    return {"message": "balikan"}

handler = Mangum(app)
