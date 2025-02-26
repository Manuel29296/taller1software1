

# Ejemplo de uso
from cubos.cubo import Cubo, CuboFlexible, CuboRigido, Empaque


if __name__ == "__main__":
    
    # Crear instancias de cubos
    cubo_rigido = CuboRigido(lado=10, valor_fabricacion=2000)
    cubo_flexible = CuboFlexible(lado=10, valor_fabricacion=2000, elasticidad=20)

    # Crear un empaque
    empaque1 = Empaque(largo=5, ancho=5, alto=100)

    # Mostrar información de los cubos
    print(cubo_rigido)  # Muestra lado y precio
    print(cubo_flexible)

    # Verificar si caben en un empaque dado
    print("Cubo Rígido cabe en empaque1:", cubo_rigido.cabe(empaque1))
    print("Cubo Rígido esta empado: ", Cubo.esta_empacado(cubo_rigido))
    print("Cubo Flexibe cabe empaque 1", cubo_flexible.cabe(empaque1))
    
    cubo_flexible.set_empaque(empaque1)
    print("Cubo Flexibe esta empado: ", Cubo.esta_empacado(cubo_flexible))

    print


                