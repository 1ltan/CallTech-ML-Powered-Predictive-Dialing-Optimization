from pydantic import BaseModel
from typing import Optional

class CustomerData(BaseModel):
    education: str
    marital_status: str
    income: float
    kidhome: int
    teenhome: int
    recency: int
    mntwines: float
    mntfruits: float
    mntmeatproducts: float
    mntfishproducts: float
    mntsweetproducts: float
    mntgoldprods: float
    numdealspurchases: int
    numwebpurchases: int
    numcatalogpurchases: int
    complain: int
    age: int
    total_children: int
    customer_for_years: float

    class Config:
        orm_mode = True

class PredictionResponse(BaseModel):
    prediction: int
    model_used: str