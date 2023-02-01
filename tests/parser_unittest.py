import unittest

import src.constant as cs
import src.parser as ps
import src.tokenizer as tk


class ParserTest(unittest.TestCase):
    def test_parser_number(self):
        parser = ps.Parser([tk.Token(cs.TokenType.NUMBER, "10")])
        output = parser.parse()
        expected = cs.Program()
        expected.body = [cs.NumberLiteral("10")]
        self.assertEqual(output, expected)

    def test_parser_string(self):
        parser = ps.Parser([tk.Token(cs.TokenType.STRING, "a-B")])
        output = parser.parse()
        expected = cs.Program()
        expected.body = [cs.StringLiteral("a-B")]
        self.assertEqual(output, expected)

    def test_parser_paren(self):
        parser = ps.Parser([
            tk.Token(cs.TokenType.PAREN, "("),
            tk.Token(cs.TokenType.NAME, "add"),
            tk.Token(cs.TokenType.PAREN, ")")
        ])
        output = parser.parse()
        expected = cs.Program()
        expected.body = [cs.CallExpression("add")]
        self.assertEqual(output, expected)

    def test_parser_paren_params(self):
        parser = ps.Parser([
            tk.Token(cs.TokenType.PAREN, "("),
            tk.Token(cs.TokenType.NAME, "add"),
            tk.Token(cs.TokenType.NUMBER, "2"),
            tk.Token(cs.TokenType.NUMBER, "4"),
            tk.Token(cs.TokenType.PAREN, ")")
        ])
        output = parser.parse()
        expected = cs.Program()
        call_expression = cs.CallExpression("add")
        call_expression.params = [cs.NumberLiteral("2"), cs.NumberLiteral("4")]
        expected.body = [call_expression]
        self.assertEqual(output, expected)
    
    def test_parser_invalid_token_error(self):
        parser = ps.Parser([tk.Token(cs.TokenType.PAREN, ")")])
        with self.assertRaises(ps.InvalidTokenTypeFoundExeception):
            parser.parse()
