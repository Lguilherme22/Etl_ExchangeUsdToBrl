import logging
from api import fetch_exchange_rates
from transform import calcular_rate_para_brl
from db_loader import inserir_rates_em_usd, inserir_rates_em_brl

logging.basicConfig(
    level=logging.INFO,
)

def main():
    rates = fetch_exchange_rates()
    if rates:
        inserir_rates_em_usd(rates)

        rates_em_brl = calcular_rate_para_brl(rates)
        if rates_em_brl:
            inserir_rates_em_brl(rates_em_brl)

    logging.info("Execução finalizada.")

if __name__ == "__main__":
    main()
