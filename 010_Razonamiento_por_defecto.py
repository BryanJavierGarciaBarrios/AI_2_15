from pyknow import *

class MotorDeRazonamientoPorDefecto(KnowledgeEngine):
    @DefFacts()
    def hechos_iniciales(self):
        yield Fact(fiebre=True)
        yield Fact(dolor_de_cabeza=True)

    @Rule(AND(Fact(fiebre=True), Fact(dolor_de_cabeza=True)))
    def conclusion(self):
        print("Podría ser gripe.")

    @Rule(AND(Fact(fiebre=False), Fact(dolor_de_cabeza=True)))
    def conclusion_2(self):
        print("Podría ser un simple dolor de cabeza.")

    @Rule(AND(Fact(fiebre=True), Fact(dolor_de_cabeza=False)))
    def conclusion_3(self):
        print("Podría ser otra enfermedad con fiebre.")

if __name__ == "__main__":
    motor = MotorDeRazonamientoPorDefecto()
    motor.reset()
    motor.declare(Fact(fiebre=True))
    motor.run()
