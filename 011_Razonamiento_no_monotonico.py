from pydefeasible import Rule, Fact, KnowledgeBase

# Crear hechos y reglas
hecho1 = Fact("Puede volar")
hecho2 = Fact("No tiene alas")
hecho3 = Fact("Es un pájaro")

regla1 = Rule([Fact("Es un pájaro")], Fact("Puede volar"), "Por defecto, los pájaros pueden volar")
regla2 = Rule([Fact("Es un pájaro"), Fact("No tiene alas")], Fact("No puede volar"), "Los pájaros sin alas no pueden volar")

# Crear la base de conocimiento
base_conocimiento = KnowledgeBase()
base_conocimiento += hecho1
base_conocimiento += hecho2
base_conocimiento += hecho3
base_conocimiento += regla1
base_conocimiento += regla2

# Realizar el razonamiento
resultados = base_conocimiento.query(Fact("Puede volar"))

# Mostrar los resultados
for resultado in resultados:
    print(resultado)
