import unittest

import src.code_generator as cg
import src.constant as cs


class CodeGeneratorTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.node = cs.TransformedProgram()
        call_expression = cs.CallExpressionWithCallee("add")
        self.node.body = [cs.ExpressionStatement(call_expression)]
        self.node.body[0].expression.arguments = [cs.NumberLiteral("2"), cs.NumberLiteral("4")]

    def test_generate_code(self):
        code_generator = cg.CodeGenerator(self.node)
        output = code_generator.generate_code()
        self.assertEqual(output, "add(2, 4);")
