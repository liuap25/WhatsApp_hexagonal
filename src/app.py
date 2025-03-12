from adapters.config import Config
from adapters.mongo import MongoConnection, MongoConversacionRepository, MongoOperacionRepository
from services.webhook import WebhookService
from adapters.web import FlaskWebhookAdapter

def setup_application():
    # Cargar configuración
    config = Config()
    
    # Configurar conexión a la base de datos
    mongo_connection = MongoConnection(config)
    if not mongo_connection:
        raise Exception("No se pudo establecer conexión con MongoDB")
    
    # Inicializar repositorios
    conversacion_repository = MongoConversacionRepository(mongo_connection)
    operacion_repository = MongoOperacionRepository(mongo_connection)
    
    # Inicializar servicios de aplicación
    webhook_service = WebhookService(conversacion_repository, operacion_repository)
    
    # Configurar adaptador web
    web_api = FlaskWebhookAdapter(webhook_service, config)
    
    return web_api, config

if __name__ == "__main__":
    web_api, config = setup_application()
    web_api.run(port=config.port, debug=True)