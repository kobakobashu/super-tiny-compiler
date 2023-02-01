import unittest

import src.tokenizer as tk
from src.constant import TokenType


class TokenizerTest(unittest.TestCase):
    def test_tokenize_space(self):
        tokenizer = tk.Tokenizer(" ")
        output = tokenizer.tokenize()
        self.assertEqual(len(output), 0)

    def test_tokenize_new_line(self):
        tokenizer = tk.Tokenizer("\n")
        output = tokenizer.tokenize()
        self.assertEqual(len(output), 0)

    def test_tokenize_number(self):
        tokenizer = tk.Tokenizer("10")
        output = tokenizer.tokenize()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0], tk.Token(TokenType.NUMBER, "10"))

    def test_tokenize_quotes(self):
        tokenizer = tk.Tokenizer("\"add\"")
        output = tokenizer.tokenize()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0], tk.Token(TokenType.STRING, "add"))

    def test_tokenize_quotes_error(self):
        tokenizer = tk.Tokenizer("\"add")
        with self.assertRaises(tk.CloseQuoteNotFoundExeception):
            tokenizer.tokenize()

    def test_tokenize_letter(self):
        tokenizer = tk.Tokenizer("a-B")
        output = tokenizer.tokenize()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0], tk.Token(TokenType.NAME, "a-B"))

    def test_tokenize_invalid_input_error(self):
        tokenizer = tk.Tokenizer("@")
        with self.assertRaises(tk.InvalidInputFoundExeception):
            tokenizer.tokenize()
