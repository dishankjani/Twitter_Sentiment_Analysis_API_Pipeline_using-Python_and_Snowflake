from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import twitter_etl
import preprocess_tweets
import sentiment_analysis

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_twitter_sentiment_analysis_dag',
    default_args=default_args,
    description='A DAG to perform Twitter sentiment analysis',
    schedule_interval=timedelta(hours=1),
)

extract_task = PythonOperator(
    task_id='twitter_etl',
    python_callable=extract_tweets.main,
    dag=dag,
)

preprocess_task = PythonOperator(
    task_id='preprocess_tweets',
    python_callable=preprocess_tweets.main,
    dag=dag,
)

sentiment_analysis_task = PythonOperator(
    task_id='sentiment_analysis',
    python_callable=sentiment_analysis.main,
    dag=dag,
)

extract_task >> preprocess_task >> sentiment_analysis_task
