import unittest

import src.constant as cs
import src.transformer as tf


class TransformerTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ast = cs.Program()
        call_expression = cs.CallExpression("add")
        call_expression.params = [cs.NumberLiteral("2"), cs.NumberLiteral("4")]
        self.ast.body = [call_expression]


    def test_transformer(self):
        expected = cs.TransformedProgram()
        call_expression = cs.CallExpressionWithCallee("add")
        expected.body = [cs.ExpressionStatement(call_expression)]
        expected.body[0].expression.arguments = [cs.NumberLiteral("2"), cs.NumberLiteral("4")]

        transfomer = tf.Transformer(self.ast)
        output = transfomer.transform()
        self.assertEqual(output, expected)
