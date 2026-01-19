from sqlalchemy import Column, Integer, String, Float, DateTime, func
from .database import Base
from datetime import datetime

class SuperstoreData(Base):
    __tablename__ = "superstore_data_cleaned"

    id = Column(Integer, primary_key=True, index=True)
    education = Column(String)
    marital_status = Column(String)
    income = Column(Float)
    kidhome = Column(Integer)
    teenhome = Column(Integer)
    recency = Column(Integer)
    mntwines = Column(Float)
    mntfruits = Column(Float)
    mntmeatproducts = Column(Float)
    mntfishproducts = Column(Float)
    mntsweetproducts = Column(Float)
    mntgoldprods = Column(Float)
    numdealspurchases = Column(Integer)
    numwebpurchases = Column(Integer)
    numcatalogpurchases = Column(Integer)
    response = Column(Integer) # Цільова
    complain = Column(Integer)
    age = Column(Integer)
    total_children = Column(Integer)
    customer_for_years = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Table models
class MLModel(Base):
    __tablename__ = "models"
    
    model_name = Column(String, primary_key=True)
    source = Column(String)
    algorithm = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Table metrics
class ModelMetrics(Base):
    __tablename__ = "model_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String)
    precision = Column(Float)
    recall = Column(Float)
    f1 = Column(Float)
    roc_auc = Column(Float)
    training_time = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    source = Column(String)

# Table predictions
class Prediction(Base):
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    prediction_result = Column(Integer)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Table inference_inputs
class InferenceInput(Base):
    __tablename__ = "inference_inputs"

    id = Column(Integer, primary_key=True, index=True)
    education = Column(String)
    marital_status = Column(String)
    income = Column(Float)
    kidhome = Column(Integer)
    teenhome = Column(Integer)
    recency = Column(Integer)
    mntwines = Column(Float)
    mntfruits = Column(Float)
    mntmeatproducts = Column(Float)
    mntfishproducts = Column(Float)
    mntsweetproducts = Column(Float)
    mntgoldprods = Column(Float)
    numdealspurchases = Column(Integer)
    numwebpurchases = Column(Integer)
    numcatalogpurchases = Column(Integer)
    complain = Column(Integer)
    age = Column(Integer)
    total_children = Column(Integer)
    customer_for_years = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)