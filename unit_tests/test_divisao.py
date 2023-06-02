import unittest
from calculator import calcular


class DivisaoTest(unittest.TestCase):

    def test_divisao(self):
        expressao = "10 / 2"
        resultado = calcular(expressao)
        self.assertEqual(resultado, 5)

