from airflow import DAG
from datetime import datetime, timedelta
from TestGetterOperator import TestGetterOperator


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 8, 15),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}


test_getter_operator_task_dag = DAG("TestGetterOperator", default_args=default_args, schedule_interval=timedelta(1))

with test_getter_operator_task_dag:
    test_getter_operator_custom_task = TestGetterOperator(task_id="test_getter_operator_custom", url="http://svn.code.sf.net/p/aper/code/phishing_reply_addresses", path='/usr/local/airflow/webpage.csv')
