from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from typing import Dict, Union, List, Any
from api import fetch_exchange_rates
from transform import calcular_rate_para_brl
from db_loader import inserir_rates_em_usd, inserir_rates_em_brl

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_taxas_cambio',
    default_args=default_args,
    description='ETL',
    schedule='@daily', 
    start_date=datetime(2025, 9, 1),
    catchup=False,
    tags=['etl', 'exchange'],
) as dag:

    def extrair() ->Dict[str,float]:
        return fetch_exchange_rates()

    def transformar(ti:Any) ->List[Dict[str,Union[str,float]]]:
        rates = ti.xcom_pull(task_ids='extrair')
        return calcular_rate_para_brl(rates)

    def carregar_usd(ti:Any) -> None:
        rates:Dict[str,float] = ti.xcom_pull(task_ids='extrair')
        inserir_rates_em_usd(rates)

    def carregar_brl(ti:Any)-> None:
        rates_brl:List[Dict[str,Union[str,float]]]= ti.xcom_pull(task_ids='transformar')
        inserir_rates_em_brl(rates_brl)

    t1 = PythonOperator(
        task_id='extrair',
        python_callable=extrair
    )

    t2 = PythonOperator(
        task_id='transformar',
        python_callable=transformar
    )

    t3 = PythonOperator(
        task_id='carregar_usd',
        python_callable=carregar_usd
    )

    t4 = PythonOperator(
        task_id='carregar_brl',
        python_callable=carregar_brl
    )


# Revisar Ordem
    t1 >> t2 >> t3  
    t2 >> t4
