import unittest

import src.constant as cs
import src.traverser as tv


class TraverserTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ast = cs.Program()
        call_expression = cs.CallExpression("add")
        call_expression.params = [cs.NumberLiteral("2"), cs.NumberLiteral("4")]
        self.ast.body = [call_expression]

    def test_traverser(self):
        expected = cs.Program()
        call_expression = cs.CallExpression("add")
        call_expression.params = [cs.NumberLiteral("2"), cs.NumberLiteral("4")]
        call_expression.context = [cs.NumberLiteral("2"), cs.NumberLiteral("4")]
        expected.body = [call_expression]
        expression = cs.CallExpressionWithCallee("add")
        expression_statement = cs.ExpressionStatement(expression)
        expression_statement.expression.arguments = [cs.NumberLiteral("2"), cs.NumberLiteral("4")]
        expected.context = [expression_statement]

        traveser = tv.Traverser(self.ast)
        traveser.traverse()
        self.assertEqual(self.ast, expected)
