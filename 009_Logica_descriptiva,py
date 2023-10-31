from owlready2 import *

# Crear una ontología
onto = Ontology("http://www.ejemplo.com/ontologia#")

# Definir clases en la ontología
class Animal(Thing):
    namespace = onto

class Mamifero(Animal):
    namespace = onto

class Ave(Animal):
    namespace = onto

# Definir propiedades y relaciones
class tiene_nombre(DataProperty, FunctionalProperty):
    namespace = onto

class es_un(ObjectProperty):
    namespace = onto
    domain = [Animal]
    range = [Animal]

# Crear instancias de clases
gato = Animal("gato")
perro = Mamifero("perro")
loro = Ave("loro")

# Asignar propiedades a instancias
gato.tiene_nombre = ["Garfield"]
perro.tiene_nombre = ["Rex"]
loro.tiene_nombre = ["Polly"]

# Establecer relaciones
gato.es_un.append(perro)

# Consultas en la ontología
with onto:
    for animal in Thing.instances():
        if "tiene_nombre" in animal.get_class_properties():
            print(f"{animal.iri}: {animal.tiene_nombre[0]}")

    for animal in Animal.instances():
        if "es_un" in animal.get_class_properties():
            print(f"{animal.iri} es un {animal.es_un[0].iri}")
