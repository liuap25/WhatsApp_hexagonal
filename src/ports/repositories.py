from abc import ABC, abstractmethod

class ConversacionRepository(ABC):
    @abstractmethod
    def find_by_phone_number(self, phone_number):
        pass

    @abstractmethod
    def save(self, conversacion):
        pass


class OperacionRepository(ABC):
    @abstractmethod
    def save(self, operacion):
        pass