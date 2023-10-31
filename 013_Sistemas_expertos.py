from pyknow import Fact, Rule, KnowledgeEngine

# Definir hechos (facts)
class Animal(Fact):
    pass

class Mamifero(Fact):
    pass

# Definir un motor de conocimiento
class SistemaExperto(KnowledgeEngine):
    @Rule(Animal(habitat='terrestre') & Animal(piel='pelo'))
    def regla1(self):
        print("Este animal podría ser un mamífero.")

    @Rule(Animal(habitat='acuático'))
    def regla2(self):
        print("Este animal no es un mamífero.")

    @Rule(Animal(piel='escamas'))
    def regla3(self):
        print("Este animal no es un mamífero.")

if __name__ == '__main__':
    engine = SistemaExperto()
    engine.reset()

    animal = Animal(habitat='terrestre', piel='pelo')
    engine.declare(animal)
    engine.run()
