import requests
import logging

logger = logging.getLogger(__name__)

API_KEY = "c30e61abcd9850dc14be64e6" #chave da api

def fetch_exchange_rates():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    
    #Faz conexão com a api
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("result") != "success":
            raise Exception(f"Erro da API: {data.get('error-type', 'Erro desconhecido')}")
        logger.info("Dados da API recebidos com sucesso!")
        return data["conversion_rates"] 
    except Exception as e:
        logger.error(f"[fetch_exchange_rates] Erro: {e}")
        return {}


if __name__ == "__main__":
    taxas = fetch_exchange_rates()
    for moeda, valor in taxas.items():
        print(f"{moeda}: {valor}")
