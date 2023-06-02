import unittest
from calculator import calcular


class ExpressaoComParentesesTest(unittest.TestCase):

    def test_expressao_com_parenteses(self):
        expressao = "(2 + 3) * (4 - 1)"
        resultado = calcular(expressao)
        self.assertEqual(resultado, 15)
