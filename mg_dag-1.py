from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

def hello_world():
    print('Hello Airflow from Python')

with DAG(
    'mg-dag-1',
    schedule_interval=None,
    start_date=days_ago(2),
    tags=['mg'],
) as dag:

    bash = BashOperator(
        task_id='bash',
        bash_command='echo Hello Airflow from Bash'
    )

    python = PythonOperator(
        task_id='python',
        python_callable=hello_world
    )

    bash >> python