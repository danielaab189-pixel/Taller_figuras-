from cuadrado import Cuadrado
from rectangulo import Rectangulo

def sumar_areas(figuras: list) -> float:
    return sum([fig.area() for fig in figuras])

def sumar_perimetros(figuras: list) -> float:
    return sum([fig.perimetro() for fig in figuras])

if __name__ == "__main__":
    # Crear objetos válidos
    c1 = Cuadrado(5)
    c2 = Cuadrado(10)
    r1 = Rectangulo(4, 6)
    r2 = Rectangulo(3, 8)

    # Intentar valores inválidosgitg
    try:
        c_invalido = Cuadrado(-2)
    except ValueError as e:
        print("Error:", e)

    # Mostrar resultados
    figuras = [c1, c2, r1, r2]
    for f in figuras:
        print(f)
        print("Área:", f.area())
        print("Perímetro:", f.perimetro())
        print("-" * 30)

    print("Suma de áreas:", sumar_areas(figuras))
    print("Suma de perímetros:", sumar_perimetros(figuras))
    