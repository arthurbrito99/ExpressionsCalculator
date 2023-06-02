import unittest
from calculator import calcular


class SomaTest(unittest.TestCase):

    def test_soma(self):
        expressao = "2+3"
        resultado = calcular(expressao)
        self.assertEqual(resultado, 5)
