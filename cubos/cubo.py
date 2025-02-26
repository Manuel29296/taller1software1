from abc import ABC, abstractmethod

# Clase para representar el empaque.
class Empaque:
    def __init__(self, largo: float, ancho: float, alto: float):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def volumen(self) -> float:
        return self.largo * self.ancho * self.alto

class Cubo(ABC):
    IVA: float = 0.19  # Público

    def __init__(self, lado: float, valor_fabricacion: float):
        self._lado: float = lado  # Atributos protegidos
        self._valor_fabricacion: float = valor_fabricacion  # Atributos protegidos
        self.__empaque: Empaque = None  # Atributo privado

    def esta_empacado(self) -> bool:
        """Indica si el cubo tiene un empaque asignado."""
        return self.__empaque is not None

    def set_empaque(self, empaque: Empaque):
        """Asigna un empaque al cubo."""
        self.__empaque = empaque

    def volumen(self) -> float:
        """Calcula el volumen del cubo (lado³)."""
        return self._lado ** 3

    def precio(self) -> float:
        """Calcula el precio del cubo según las reglas específicas."""
        return self._valor_fabricacion * (1 + Cubo.IVA)

    @abstractmethod
    def cabe(self, empaque: Empaque) -> bool:
        """Determina si el cubo cabe en el empaque dado."""
        pass

    def __str__(self) -> str:
        return f"Lado: {self._lado}, Precio: {self.precio():.2f}"

class CuboRigido(Cubo):
    def __init__(self, lado: float, valor_fabricacion: float):
        super().__init__(lado, valor_fabricacion)
    
    def cabe(self, empaque: Empaque) -> bool:
        return empaque.largo > self._lado and empaque.ancho > self.lado and empaque.alto > self.lado

class CuboFlexible(Cubo):
    def __init__(self, lado: float, valor_fabricacion: float, elasticidad: int):
        super().__init__(lado, valor_fabricacion)
        self.elasticidad = elasticidad
    
    def cabe(self, empaque: Empaque) -> bool:
        return empaque.volumen() > self.volumen()
    
    def precio(self) -> float:
        precio_base = super().precio()
        incremento = 0.04 if self.elasticidad < 50 else 0.06
        return precio_base * (1 + incremento)
    


