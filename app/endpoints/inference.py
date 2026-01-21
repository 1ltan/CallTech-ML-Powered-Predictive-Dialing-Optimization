from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import database, crud
from ..schemas import CustomerData, PredictionResponse
from ..services import model
import pandas as pd

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict(input_data: CustomerData, db: Session = Depends(database.get_db)):
    data_dict = input_data.dict()
    df_input = pd.DataFrame([data_dict])
    
    ml_service = model.CallTechModel()
    try:
        prediction = ml_service.predict(df_input)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    crud.save_prediction(db, prediction, source="inference")
    crud.save_inference_input(db, data_dict)
    return {"prediction": int(prediction), "model_used": ml_service.model_name}