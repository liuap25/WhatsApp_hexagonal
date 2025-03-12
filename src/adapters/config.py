import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.webhook_verify_token = os.getenv("WEBHOOK_VERIFY_TOKEN")
        self.graph_api_token = os.getenv("GRAPH_API_TOKEN")
        self.mongo_uri = os.getenv("MONGO_URI")
        self.mongo_db_name = os.getenv("MONGO_DB_NAME")
        self.port = int(os.getenv("PORT", 8080))