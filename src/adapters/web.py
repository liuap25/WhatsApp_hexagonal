from flask import Flask, request, jsonify

class FlaskWebhookAdapter:
    def __init__(self, webhook_service, config):
        self.app = Flask(__name__)
        self.webhook_service = webhook_service
        self.config = config
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route("/webhook", methods=["POST"])
        def handle_webhook():
            data = request.get_json()
            print("📥 Incoming webhook message:", data)
            
            message = data.get("entry", [{}])[0].get("changes", [{}])[0].get("value", {}).get("messages", [{}])[0]
            contact = data.get("entry", [{}])[0].get("changes", [{}])[0].get("value", {}).get("contacts", [{}])[0]
            metadata = data.get("entry", [{}])[0].get("changes", [{}])[0].get("value", {}).get("metadata", {})
            
            self.webhook_service.process_message(message, contact, metadata)
            return jsonify({"status": "received"}), 200

        @self.app.route("/webhook", methods=["GET"])
        def verify_webhook():
            mode = request.args.get("hub.mode")
            token = request.args.get("hub.verify_token")
            challenge = request.args.get("hub.challenge")
            
            result, status_code = self.webhook_service.verify_token(
                mode, token, challenge, self.config.webhook_verify_token
            )
            return result, status_code

        @self.app.route("/", methods=["GET"])
        def home():
            return "<h1>✅ Servidor en funcionamiento.</h1>"

    def run(self, port, debug=False):
        self.app.run(port=port, debug=debug)