
# Taller Figuras Geométricas (POO en Python)

Este proyecto implementa clases en Python aplicando **POO**:
- Encapsulamiento con `@property` y `@setter`
- Herencia y sobrescritura de métodos
- Validaciones internas
- Estándar PEP8

## 📂 Clases
- **FiguraGeometrica**: clase base con atributos `ancho` y `alto`.
- **Cuadrado**: hereda de FiguraGeometrica, recibe un solo parámetro `lado`.
- **Rectangulo**: hereda de FiguraGeometrica, recibe `ancho` y `alto`.

## 📊 Ejecución
El programa principal (`main.py`) crea cuadrados y rectángulos, muestra:
- Área
- Perímetro
- Validación de errores
- Impresión de objetos

## 🖼️ Evidencia
<img width="1920" height="1080" alt="Captura de pantalla 2025-11-21 005510" src="https://github.com/user-attachments/assets/bec4f6fa-4ebd-4200-b095-ec314bcd4249" />

classDiagram
    class FiguraGeometrica {
        -_ancho: float
        -_alto: float
        +_init_(ancho, alto)
        +ancho: property (getter/setter)
        +alto: property (getter/setter)
        +area() float
        +perimetro() NotImplementedError
        +_str_() str
    }
    
    class Cuadrado {
        +_init_(lado)
        +area() float
        +perimetro() float
        +_str_() str
    }
    
    class Rectangulo {
        +_init_(ancho, alto)
        +area() float
        +perimetro() float
        +_str_() str
    }
    
    FiguraGeometrica <|-- Cuadrado : hereda
    FiguraGeometrica <|-- Rectangulo : hereda
    
