class FiguraGeometrica:
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    # Encapsulamiento con property
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor: float):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor: float):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = valor

    def area(self) -> float:
        return self.ancho * self.alto

    def perimetro(self):
        # Método abstracto (no implementado)
        pass

    def __str__(self):
        return f"FiguraGeometrica(ancho={self.ancho}, alto={self.alto})"