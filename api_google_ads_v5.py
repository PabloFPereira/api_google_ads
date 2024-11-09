import os
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
import json
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "google-ads.yaml")
    
    if not os.path.exists(config_path):
        logger.error(f"Arquivo de configuração não encontrado: {config_path}")
        return
    
    logger.info(f"Usando configuração de: {config_path}")
    
    try:
        client = GoogleAdsClient.load_from_storage(config_path)
        client.login_customer_id = "xxxxxxxxxxxxxxxx"  # aqui informe sua conta de gerenciamento
        logger.info("Cliente do Google Ads carregado com sucesso.")
    except Exception as e:
        logger.error("Erro ao carregar o cliente do Google Ads:", exc_info=True)
        return
    
    customer_id = "xxxxxxxxxxxxxxxx"  # aqui informe sua conta de anuncio
    
   
    start_date = "2024-10-01"  
    end_date = "2024-10-01"

    
    query = f"""
        SELECT
            campaign.id,
            campaign.name,
            campaign_budget.amount_micros,
            segments.date,
            metrics.cost_micros,
            metrics.clicks,
            metrics.impressions,
            metrics.conversions,
            metrics.conversions_value,
            metrics.conversions_from_interactions_rate,
            campaign.bidding_strategy_type
        FROM
            campaign
        WHERE
            segments.date BETWEEN '{start_date}' AND '{end_date}'
        ORDER BY
            segments.date
    """
    
    try:
        google_ads_service = client.get_service("GoogleAdsService")
        response = google_ads_service.search(
            customer_id=customer_id,
            query=query
        )
        
        ads_data = []
        for row in response:
        
            cost = row.metrics.cost_micros / 1_000_000 if row.metrics.cost_micros else 0
            budget = row.campaign_budget.amount_micros / 1_000_000 if row.campaign_budget.amount_micros else 0
            
            
            date = row.segments.date
            
            ad_entry = {
                "id_campanha": row.campaign.id,
                "nome_campanha": row.campaign.name,
                "data_consulta": date,
                "orçamento_planejado": budget,
                "custo": cost,
                "cliques": row.metrics.clicks,
                "impressoes": row.metrics.impressions,
                "conversoes": row.metrics.conversions,
                "valor_conversoes": row.metrics.conversions_value,
                "taxa_de_conversao_por_interacao": row.metrics.conversions_from_interactions_rate,
                "estrategia_lancamento": row.campaign.bidding_strategy_type.name
            }
            ads_data.append(ad_entry)
        
        if not ads_data:
            logger.info("Nenhum dado encontrado para a consulta.")
        else:
            
            with open('google_ads_data.json', 'w', encoding='utf-8') as f:
                json.dump(ads_data, f, ensure_ascii=False, indent=4)
            logger.info(f"{len(ads_data)} registros salvos em google_ads_data.json")
    
    except GoogleAdsException as ex:
        logger.error(f"Erro na API do Google Ads: {ex}")
        for error in ex.failure.errors:
            logger.error(f"\t{error.message}")
    except Exception as e:
        logger.error("Erro inesperado:", exc_info=True)

if __name__ == "__main__":
    main()