import pandas as pd
import numpy as np
import joblib
import os
import time
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

class CallTechModel:
    def __init__(self):
        self.model_name = "Logistic Regression"
        self.model_path = os.path.join(MODEL_DIR, f"{self.model_name}.pkl")
        self.model = None

    def train(self, df: pd.DataFrame, test_size=0.2):
        start_time = time.time()
        
        X = df.drop(columns=['response'])
        y = df['response']
        
        cat_features = ['education', 'marital_status']
        num_features = [c for c in X.columns if c not in cat_features]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), num_features),
                ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
            ])
        
        pipeline = ImbPipeline([
            ('preprocessor', preprocessor),
            ('smote', SMOTE(random_state=42)),
            ('classifier', LogisticRegression(max_iter=1000))
        ])
        
        param_dist = {
            'classifier__C': np.logspace(-3, 3, 7),
            'classifier__penalty': ['l2']
        }

        pipeline.fit(X_train, y_train)
        y_pred_base = pipeline.predict(X_test)

        search = RandomizedSearchCV(pipeline, param_distributions=param_dist, n_iter=10, cv=3, scoring='f1', random_state=42)
        search.fit(X_train, y_train)
        
        best_model = search.best_estimator_
        self.model = best_model
       
        y_pred = best_model.predict(X_test)
        y_prob = best_model.predict_proba(X_test)[:, 1]
        
        metrics = {
            "model_name": self.model_name,
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "f1": f1_score(y_test, y_pred),
            "roc_auc": roc_auc_score(y_test, y_prob),
            "training_time": time.time() - start_time,
            "source": "training_process"
        }
        
        print("Tuned F1:", metrics['f1'])
        joblib.dump(self.model, self.model_path)
        return metrics, best_model.predict(X) 

    def load(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
        else:
            raise Exception("Model not found.")

    def predict(self, data: pd.DataFrame):
        if not self.model:
            self.load()
        return self.model.predict(data)