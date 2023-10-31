from pyswip import Prolog

# Crear un objeto Prolog
prolog = Prolog()

# Definir reglas
prolog.assertz("humano(socrates)")
prolog.assertz("humano(platon)")
prolog.assertz("mortal(X) :- humano(X)")

# Consultas en la base de conocimiento
for solucion in prolog.query("mortal(X)"):
    print(f"{solucion['X']} es mortal.")

for solucion in prolog.query("humano(X)"):
    print(f"{solucion['X']} es un humano.")
