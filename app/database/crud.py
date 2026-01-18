from sqlalchemy.orm import Session
import pandas as pd
from . import models

def get_training_data(db: Session):
    query = db.query(models.SuperstoreData)
    return pd.read_sql(query.statement, db.bind)

def save_model_metadata(db: Session, name: str, algorithm: str, source: str):
    db_model = models.MLModel(model_name=name, algorithm=algorithm, source=source)
    db.merge(db_model)
    db.commit()

def save_metrics(db: Session, metrics: dict):
    db_metric = models.ModelMetrics(**metrics)
    db.add(db_metric)
    db.commit()

def save_prediction(db: Session, result: int, source: str):
    db_pred = models.Prediction(prediction_result=int(result), source=source)
    db.add(db_pred)
    db.commit()

def save_inference_input(db: Session, data: dict):
    db_input = models.InferenceInput(**data)
    db.add(db_input)
    db.commit()

def get_reference_data(db: Session):
    return get_training_data(db)

def get_current_data(db: Session):
    query = db.query(models.InferenceInput)
    return pd.read_sql(query.statement, db.bind)