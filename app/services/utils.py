import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset, TargetDriftPreset
from evidently.metrics import ClassificationQualityMetric

def prepare_data_for_training(df: pd.DataFrame):
    cols_to_check = [c for c in df.columns if c not in ['id', 'timestamp']]
    df_clean = df.drop_duplicates(subset=cols_to_check).copy()
    
    if 'id' in df_clean.columns:
        df_clean = df_clean.drop(columns=['id'])
    if 'timestamp' in df_clean.columns:
        df_clean = df_clean.drop(columns=['timestamp'])
        
    return df_clean

def generate_evidently_report(reference_data: pd.DataFrame, current_data: pd.DataFrame, target_col='response'):
    common_cols = [c for c in reference_data.columns if c in current_data.columns and c != 'id']
    
    ref = reference_data[common_cols].copy()
    cur = current_data[common_cols].copy()
    
    # Report generation
    report = Report(metrics=[
        DataDriftPreset(), 
        DataQualityPreset()
    ])
    
    report.run(reference_data=ref, current_data=cur)
    report.save_html("data_drift_report.html")
    return "Report generated: data_drift_report.html"