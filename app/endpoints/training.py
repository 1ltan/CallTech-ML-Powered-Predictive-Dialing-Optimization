from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import database, crud
from ..services import model, utils

router = APIRouter()

@router.post("/train-model")
def train_model(test_split: float = 0.2, db: Session = Depends(database.get_db)):
    df = crud.get_training_data(db)
    if df.empty:
        raise HTTPException(status_code=404, detail="No training data found")
    
    df_clean = utils.prepare_data_for_training(df)
    
    ml_service = model.CallTechModel()
    metrics, all_predictions = ml_service.train(df_clean, test_size=test_split)

    crud.save_metrics(db, metrics)
    crud.save_model_metadata(db, ml_service.model_name, "Logistic Regression", "train")

    for pred in all_predictions:
        crud.save_prediction(db, int(pred), source="train")
    return {"message": "Training completed", "metrics": metrics}