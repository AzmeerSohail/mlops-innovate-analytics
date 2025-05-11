from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

def retrain_model():
    subprocess.call(['python', 'train_model.py'])

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

with DAG('retrain_model', default_args=default_args, schedule_interval='@daily') as dag:
    retrain_task = PythonOperator(
        task_id='retrain_model',
        python_callable=retrain_model
    )
