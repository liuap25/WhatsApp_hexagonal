from pymongo import MongoClient
from pymongo.server_api import ServerApi
from domain.models import Conversacion, Operacion
from ports.repositories import ConversacionRepository, OperacionRepository

class MongoConnection:
    _instance = None

    def __new__(cls, config):
        if cls._instance is None:
            cls._instance = super(MongoConnection, cls).__new__(cls)
            try:
                cls._instance.client = MongoClient(config.mongo_uri, server_api=ServerApi('1'))
                cls._instance.db = cls._instance.client[config.mongo_db_name]
                print("✅ Conectado exitosamente a MongoDB Atlas")
            except Exception as e:
                print(f"❌ Error al conectar a MongoDB: {e}")
                cls._instance = None
        return cls._instance


class MongoConversacionRepository(ConversacionRepository):
    def __init__(self, mongo_connection):
        self.collection = mongo_connection.db["conversaciones"]

    def find_by_phone_number(self, phone_number):
        data = self.collection.find_one({"cliente_phone_number": phone_number})
        if data:
            return Conversacion(
                id=data["_id"],
                operador_name=data["operador_name"],
                operador_phone_number=data["operador_phone_number"],
                cliente_name=data["cliente_name"],
                cliente_phone_number=data["cliente_phone_number"],
                cliente_country_phone_number=data["cliente_country_phone_number"],
                process_state=data["process_state"],
                process_start_date=data["process_start_date"],
                process_end_date=data.get("process_end_date", ""),
                process_retry=data.get("process_retry", "")
            )
        return None

    def save(self, conversacion):
        self.collection.insert_one(conversacion.to_dict())


class MongoOperacionRepository(OperacionRepository):
    def __init__(self, mongo_connection):
        self.collection = mongo_connection.db["operaciones"]

    def save(self, operacion):
        self.collection.insert_one(operacion.to_dict())
