import unittest
from calculator import calcular


class ExpressaoComplexaTest(unittest.TestCase):

    def test_expressao_complexa(self):
        expressao = "5 * (4 + 2) - 8 / (1 + 3)"
        resultado = calcular(expressao)
        self.assertEqual(resultado, 27)
