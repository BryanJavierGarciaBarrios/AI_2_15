class Frame:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def __str__(self):
        return f"{self.name}: {self.attributes}"

# Clase para representar eventos
class Event(Frame):
    def __init__(self, name, attributes):
        super().__init__(name, attributes)

# Crear instancias de eventos
event1 = Event("Encender luz", {"ubicación": "Sala de estar", "intensidad": "alta"})
event2 = Event("Apagar luz", {"ubicación": "Dormitorio", "intensidad": "baja"})
event3 = Event("Abrir puerta", {"ubicación": "Entrada principal", "hora": "15:00"})

# Imprimir información de eventos
print("Eventos:")
print(event1)
print(event2)
print(event3)
