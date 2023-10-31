# Definición de una clase de marco (Frame)
class Frame:
    def __init__(self):
        self.properties = {}  # Diccionario para almacenar propiedades del marco

    def add_property(self, property_name, value):
        self.properties[property_name] = value

    def get_property(self, property_name):
        return self.properties.get(property_name, None)

    def __str__(self):
        return str(self.properties)

# Creación de instancias de marcos
objeto1 = Frame()
objeto2 = Frame()

# Agregar propiedades a los marcos
objeto1.add_property("nombre", "Pelota")
objeto1.add_property("color", "rojo")
objeto1.add_property("tamaño", "pequeño")

objeto2.add_property("nombre", "Coche")
objeto2.add_property("color", "azul")
objeto2.add_property("tamaño", "grande")

# Definición de una situación
class Situation:
    def __init__(self):
        self.frames = []  # Lista de marcos en la situación

    def add_frame(self, frame):
        self.frames.append(frame)

    def __str__(self):
        return "\n".join([str(frame) for frame in self.frames])

# Creación de una instancia de situación
situacion = Situation()

# Agregar los marcos a la situación
situacion.add_frame(objeto1)
situacion.add_frame(objeto2)

# Mostrar la situación
print("Situación:")
print(situacion)
