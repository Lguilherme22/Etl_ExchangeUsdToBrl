import logging

logger = logging.getLogger(__name__)
#Transformação das taxas pra Brl
def calcular_rate_para_brl(rates):
    try:
        usd_to_brl = rates.get("BRL") #pego o valor da taxa do real
        if usd_to_brl is None:
            raise ValueError("Taxa USD não encontrada")# caso nao ache o real, da erro

        rates_em_brl = {
            moeda: round(usd_to_brl / taxa, 3) #calculo da taxa do real / por taxa de outra moeda
            for moeda, taxa in rates.items()
            if moeda != "BRL"
        }

        logger.info("Transformação realizada com sucesso")
        return rates_em_brl

    except Exception as e:
        logger.error(f"[calcular_rate_para_brl] Erro: {e}")
        return {}
