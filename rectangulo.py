from figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho: float, alto: float):
        super().__init__(ancho, alto)

    def area(self) -> float:
        return self.ancho * self.alto

    def perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)

    def __str__(self):
        return f"Rectangulo(ancho={self.ancho}, alto={self.alto})"