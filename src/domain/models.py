class Conversacion:
    def __init__(self, id, operador_name, operador_phone_number, 
                 cliente_name, cliente_phone_number, cliente_country_phone_number, 
                 process_state, process_start_date, process_end_date="", process_retry=""):
        self.id = id
        self.operador_name = operador_name
        self.operador_phone_number = operador_phone_number
        self.cliente_name = cliente_name
        self.cliente_phone_number = cliente_phone_number
        self.cliente_country_phone_number = cliente_country_phone_number
        self.process_state = process_state
        self.process_start_date = process_start_date
        self.process_end_date = process_end_date
        self.process_retry = process_retry

    def to_dict(self):
        return {
            "_id": self.id,
            "operador_name": self.operador_name,
            "operador_phone_number": self.operador_phone_number,
            "cliente_name": self.cliente_name,
            "cliente_phone_number": self.cliente_phone_number,
            "cliente_country_phone_number": self.cliente_country_phone_number,
            "process_state": self.process_state,
            "process_start_date": self.process_start_date,
            "process_end_date": self.process_end_date,
            "process_retry": self.process_retry
        }


class Operacion:
    def __init__(self, conversacion_id, fecha_hora, flujo, mensaje):
        self.conversacion_id = conversacion_id
        self.fecha_hora = fecha_hora
        self.flujo = flujo
        self.mensaje = mensaje

    def to_dict(self):
        return {
            "conversacion_id": self.conversacion_id,
            "FechaHora": self.fecha_hora,
            "Flujo": self.flujo,
            "Mensaje": self.mensaje
        }


# /src/ports/__init__.py
# Este archivo puede estar vacío
