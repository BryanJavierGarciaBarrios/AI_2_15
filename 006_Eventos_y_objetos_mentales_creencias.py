class Creencia:
    def __init__(self, nombre, contenido):
        self.nombre = nombre
        self.contenido = contenido

    def __str__(self):
        return f"{self.nombre}: {self.contenido}"

class SistemaMental:
    def __init__(self):
        self.creencias = []

    def agregar_creencia(self, creencia):
        self.creencias.append(creencia)

    def eliminar_creencia(self, nombre):
        self.creencias = [creencia for creencia in self.creencias if creencia.nombre != nombre]

    def actualizar_creencia(self, nombre, nuevo_contenido):
        for creencia in self.creencias:
            if creencia.nombre == nombre:
                creencia.contenido = nuevo_contenido

    def ver_creencias(self):
        print("Creencias actuales:")
        for creencia in self.creencias:
            print(creencia)

# Crear un sistema mental
sistema_mental = SistemaMental()

# Agregar creencias iniciales
sistema_mental.agregar_creencia(Creencia("Ubicación", "Casa"))
sistema_mental.agregar_creencia(Creencia("Estado de Ánimo", "Feliz"))

# Ver las creencias iniciales
sistema_mental.ver_creencias()

# Actualizar una creencia
sistema_mental.actualizar_creencia("Estado de Ánimo", "Motivado")

# Agregar una nueva creencia
sistema_mental.agregar_creencia(Creencia("Tarea Pendiente", "Reunión a las 14:00"))

# Ver las creencias actualizadas
sistema_mental.ver_creencias()

# Eliminar una creencia
sistema_mental.eliminar_creencia("Ubicación")

# Ver las creencias actualizadas
sistema_mental.ver_creencias()
