import logging
from config.db_config import get_connection
from datetime import datetime

logger = logging.getLogger(__name__)

def inserir_rates_em_usd(rates):
    now = datetime.now()
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                for moeda, taxa in rates.items():
                    cursor.execute("""
                        INSERT INTO exchange_usd_rates (
                            description, datetime, float_rate
                        ) VALUES (%s, %s, %s)
                        ON CONFLICT (description, datetime) DO NOTHING;
                    """, (moeda, now, taxa))
            conn.commit()
        logger.info("Dados USD inseridos com sucesso.")
    except Exception as e:
        logger.error(f"[inserir_rates_em_usd] erro ao inserir: {e}")

def inserir_rates_em_brl(rates_em_brl):
    now = datetime.now()
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                for moeda, taxa in rates_em_brl.items():
                    cursor.execute("""
                        INSERT INTO exchange_real_rates (
                            description_coin, datetime_rate, float_rate, etl_created_at, etl_updated_at
                        ) VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (description_coin, datetime_rate) DO UPDATE
                        SET float_rate = EXCLUDED.float_rate,
                            etl_updated_at = EXCLUDED.etl_updated_at;
                    """, (moeda, now, taxa, now, now))
            conn.commit()
        logger.info("Dados BRL inseridos com sucesso.")
    except Exception as e:
        logger.error(f"[inserir_rates_em_brl] Erro ao inserir: {e}")
