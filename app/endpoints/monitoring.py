from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import database, crud
from ..services import utils

router = APIRouter()

@router.get("/generate-report")
def generate_report(db: Session = Depends(database.get_db)):
    ref_data = crud.get_reference_data(db)
    curr_data = crud.get_current_data(db)
    ref_data = utils.prepare_data_for_training(ref_data)
    if 'id' in curr_data.columns:
        curr_data = curr_data.drop(columns=['id'])
    if 'timestamp' in curr_data.columns:
        curr_data = curr_data.drop(columns=['timestamp'])
        
    msg = utils.generate_evidently_report(ref_data, curr_data)
    return {"message": msg}