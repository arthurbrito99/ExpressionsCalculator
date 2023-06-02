import unittest
from calculator import calcular


class MultiplicacaoTest(unittest.TestCase):

    def test_multiplicacao(self):
        expressao = "2 * 4"
        resultado = calcular(expressao)
        self.assertEqual(resultado, 8)
