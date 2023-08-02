class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def perimetro(self):
        pass

    def area(self):
        pass

    def mostrar_figura(self):
        print(f"Figura: {self.nombre}")


class Cuadrado(Figura):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.lado = float(input("Ingrese el valor del lado del cuadrado: "))

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado ** 2


class Rectangulo(Figura):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.base = float(input("Ingrese el valor de la base del rectángulo: "))
        self.altura = float(input("Ingrese el valor de la altura del rectángulo: "))

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def area(self):
        return self.base * self.altura


if __name__ == "__main__":
    # Crear una instancia de Cuadrado y probar sus métodos
    cuadrado = Cuadrado("Cuadrado")
    cuadrado.mostrar_figura()
    print("Perímetro:", cuadrado.perimetro())
    print("Área:", cuadrado.area())

    # Crear una instancia de Rectángulo y probar sus métodos
    rectangulo = Rectangulo("Rectángulo")
    rectangulo.mostrar_figura()
    print("Perímetro:", rectangulo.perimetro())
    print("Área:", rectangulo.area())
