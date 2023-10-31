class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []
        self.objetos = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def __str__(self, nivel=0):
        resultado = "  " * nivel + self.nombre + "\n"
        for subcategoria in self.subcategorias:
            resultado += subcategoria.__str__(nivel + 1)
        for objeto in self.objetos:
            resultado += "  " * (nivel + 1) + objeto + "\n"
        return resultado

# Crear categorías y objetos en una taxonomía
raiz = Categoria("Dominio")
categoria1 = Categoria("Categoría 1")
categoria2 = Categoria("Categoría 2")
objeto1 = "Objeto 1"
objeto2 = "Objeto 2"

# Establecer relaciones jerárquicas
raiz.agregar_subcategoria(categoria1)
raiz.agregar_subcategoria(categoria2)
categoria1.agregar_objeto(objeto1)
categoria2.agregar_objeto(objeto2)

# Imprimir la taxonomía
print(raiz)
