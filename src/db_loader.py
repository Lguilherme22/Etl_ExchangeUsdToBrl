import logging
from config.db_config import get_connection
from datetime import datetime
import psycopg2.extras 
from typing import Dict, Union, List, Any,Tuple

logger = logging.getLogger(__name__)

ratetype = Dict[str,float]
raterealtype = Dict[str,Union[str,float]]

def inserir_rates_em_usd(rates:ratetype):
    now = datetime.now()
    
   
    data_list_of_tuples:List[Tuple[str,datetime,float]] = [
        (moeda, now, taxa)
        for moeda, taxa in rates.items()
    ]
    
  #inserção de dados na tabela exchange_usd
    insert_query = """
        INSERT INTO exchange_usd_rates (
            description, datetime, float_rate
        ) VALUES %s
        ON CONFLICT (description, datetime) DO NOTHING;
    """
    
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                
                psycopg2.extras.execute_values(
                    cursor, 
                    insert_query, 
                    data_list_of_tuples, 
                    page_size=1000 
                )
            conn.commit()
        logger.info("Dados USD inseridos com sucesso (batch).")
    except Exception as e:
        logger.error(f"[inserir_rates_em_usd] erro ao inserir batch: {e}")
        raise e


def inserir_rates_em_brl(rates_em_brl:raterealtype):
    now = datetime.now()
   
    data_list_of_tuples: List[Tuple[str,datetime,Union[str,float,datetime,datetime]]] = [
        (moeda, now, taxa, now, now)
        for moeda, taxa in rates_em_brl.items()
    ]
    
   #inserção de dados na tabela exchange_brl 
    insert_query = """
    INSERT INTO exchange_real_rates (
        description_coin, datetime_rate, float_rate, etl_created_at, etl_updated_at
    ) VALUES %s  
    ON CONFLICT (description_coin, datetime_rate) DO UPDATE
    SET float_rate = EXCLUDED.float_rate,
        etl_updated_at = EXCLUDED.etl_updated_at;
"""

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                
                psycopg2.extras.execute_values(
                    cursor, 
                    insert_query, 
                    data_list_of_tuples, 
                    page_size=1000 
                )
            conn.commit()
        logger.info("Dados BRL inseridos com sucesso (batch).") #caso sucesso, insira
    except Exception as e:
        logger.error(f"[inserir_rates_em_brl] Erro ao inserir batch: {e}")#caso falha, pare
        raise e 