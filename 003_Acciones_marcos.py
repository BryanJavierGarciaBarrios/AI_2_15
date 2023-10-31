# Definición de una clase de marco para representar un animal
class AnimalFrame:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def describe(self):
        return f"{self.name} es un {self.species} de {self.age} años de edad."

# Definición de una clase de acción para representar acciones que un animal puede realizar
class Action:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def perform(self, subject):
        return f"{subject.name} {self.description}"

# Crear instancias de marcos (objetos)
dog = AnimalFrame("Max", "perro", 3)
cat = AnimalFrame("Whiskers", "gato", 5)

# Crear instancias de acciones
action1 = Action("comer", "está comiendo su comida.")
action2 = Action("dormir", "está durmiendo en su cama.")
action3 = Action("jugar", "está jugando con una pelota.")

# Ejecutar acciones en los marcos
print(action1.perform(dog))  # Max está comiendo su comida.
print(action2.perform(cat))  # Whiskers está durmiendo en su cama.

# Describir los marcos
print(dog.describe())  # Max es un perro de 3 años de edad.
print(cat.describe())  # Whiskers es un gato de 5 años de edad.
