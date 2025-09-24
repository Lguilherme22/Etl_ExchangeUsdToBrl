import logging

logger = logging.getLogger(__name__)

def calcular_rate_para_brl(rates):
    try:
        usd_to_brl = rates.get("BRL")
        if usd_to_brl is None:
            raise ValueError("Taxa USD não encontrada")

        rates_em_brl = {
            moeda: round(usd_to_brl / taxa, 3)
            for moeda, taxa in rates.items()
            if moeda != "BRL"
        }

        logger.info("Transformação realizada com sucesso")
        return rates_em_brl

    except Exception as e:
        logger.error(f"[calcular_rate_para_brl] Erro: {e}")
        return {}
