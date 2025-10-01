import logging
from typing import Dict,Union
logger = logging.getLogger(__name__)

ratetype = Dict[str,float]



#Transformação das taxas pra Brl
def calcular_rate_para_brl(rates:ratetype):
    try:
        usd_to_brl = rates.get("BRL") #pego o valor da taxa do real
        if usd_to_brl is None:
            raise ValueError("Taxa USD não encontrada")# caso nao ache o real, da erro

        rates_em_brl:ratetype = {
            moeda: round(usd_to_brl / taxa, 3) #calculo da taxa do real / por taxa de outra moeda
            for moeda, taxa in rates.items()
            if moeda != "BRL"
        }

        logger.info("Transformação realizada com sucesso")
        return rates_em_brl

    except Exception as e:
        logger.error(f"[calcular_rate_para_brl] Erro: {e}")
        return {}
