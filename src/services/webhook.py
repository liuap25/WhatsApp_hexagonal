from datetime import datetime
from domain.models import Conversacion, Operacion

class WebhookService:
    def __init__(self, conversacion_repository, operacion_repository):
        self.conversacion_repository = conversacion_repository
        self.operacion_repository = operacion_repository

    def process_message(self, message_data, contact_data, metadata):
        message = message_data
        contact = contact_data
        business_phone_number_id = metadata.get("phone_number_id", "")
        
        if message.get("type") == "text":
            sender_id = message["from"]
            sender_name = contact.get("profile", {}).get("name", "Desconocido")
            message_text = message["text"]["body"]
            message_id = message["id"]
            timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

            # Identificar si el mensaje es del cliente o de la empresa
            flujo = "Cliente" if sender_id != business_phone_number_id else "Empresa"

            # Buscar si ya existe una conversación con este cliente
            conversation = self.conversacion_repository.find_by_phone_number(sender_id)

            if not conversation:
                conversation_id = message_id  # Usar el message_id como ID inicial de la conversación
                nueva_conversacion = Conversacion(
                    id=conversation_id,
                    operador_name="Test Bot",
                    operador_phone_number=business_phone_number_id,
                    cliente_name=sender_name,
                    cliente_phone_number=sender_id,
                    cliente_country_phone_number="+51",
                    process_state="3",
                    process_start_date=timestamp
                )
                self.conversacion_repository.save(nueva_conversacion)
            else:
                conversation_id = conversation.id

            print(f"✅ ID de conversación asignado: {conversation_id}")

            # Guardar el mensaje en `operaciones`
            operacion = Operacion(
                conversacion_id=conversation_id,
                fecha_hora=timestamp,
                flujo=flujo,
                mensaje=message_text
            )
            self.operacion_repository.save(operacion)

            return True
        return False
        
    def verify_token(self, mode, token, challenge, webhook_verify_token):
        if mode == "subscribe" and token == webhook_verify_token:
            return challenge, 200
        else:
            return "Forbidden", 403