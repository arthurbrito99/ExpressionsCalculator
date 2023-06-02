import unittest
from calculator import calcular


class SubtracaoTest(unittest.TestCase):

    def test_subtracao(self):
        expressao = "5 - 3"
        resultado = calcular(expressao)
        self.assertEqual(resultado, 2)
