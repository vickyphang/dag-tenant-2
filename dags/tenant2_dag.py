from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'tenant2',
    'start_date': datetime(2025, 3, 6),
}

with DAG('tenant2_dag', default_args=default_args, schedule_interval='@daily') as dag:
    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task3 = DummyOperator(task_id='task3')
    task1 >> task2 >> task3