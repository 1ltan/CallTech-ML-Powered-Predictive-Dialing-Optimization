from fastapi import FastAPI
from .database import models, database
from .endpoints import training, inference, monitoring

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="CallTech ML API")

app.include_router(training.router, tags=["Training"])
app.include_router(inference.router, tags=["Inference"])
app.include_router(monitoring.router, tags=["Monitoring"])

@app.get("/")
def root():
    return {"message": "CallTech ML API is running"}