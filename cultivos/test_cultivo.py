from unittest import TestCase
from cultivos.cultivo import Cultivo

class TetsCultivo(TestCase):
    def test_calcular_consumo_tipo_t(self):
        cultivo=Cultivo()
        consumo = cultivo.calcular_consumo(32,"t")
        self.assertEqual(consumo, 16)
        
    def test_calcular_consumo_tipo_h(self):
        area =23
        tipo = "h"

    def test_validar_area_negativa(self):
        area =-2
        tipo = "t"

    def test_calcular_consumo_tipo_no_registrado(self):
        area =15
        tipo = "j"

