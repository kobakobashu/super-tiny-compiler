from typing import List

from src import constant
from src.tokenizer import Token


class ParserIndexExeception(Exception):
    """Raised when the index is out of range."""
    pass


class InvalidTokenTypeFoundExeception(Exception):
    """Raised when the tokens contains unexpected TokenType."""
    pass


class Parser:
    def __init__(self, tokens: List['Token']) -> None:
        """Inits Parser.

        Args:
            tokens: A list of Token like [Token(type: 'paren', value: '('), ...]
        """
        self.tokens = tokens
        self.current_idx = 0
        self.ast = constant.Program()
    
    def parse(self) -> constant.Program:
        """Function to make an Abstract Syntax Tree from self.tokens.

        Returns:
            constant.Program: A instance of Program.
            Example:
                Program(
                    type: 'Program',
                    body:[
                        type: 'CallExpression',
                        value: 'add',
                        params: ..
                    ]
                )
        """
        while self.current_idx < len(self.tokens):
            self.ast.body.append(self.walk_tokens())

        return self.ast

    def walk_tokens(self) -> constant.Node:
        """Function to look self.tokens and match it to the corresponding node class.

        Returns:
            Node: An instance of the class.
                  The class is one of [NumberLiteral, StringLiteral, CallExpression, Program]
        Raises:
            ParserIndexExeception: Raised when the index is out of range
        """
        token = self.get_token()

        if token.token_type == constant.TokenType.NUMBER:
            self.current_idx += 1
            return constant.NumberLiteral(token.token_value)

        if token.token_type == constant.TokenType.STRING:
            self.current_idx += 1
            return constant.StringLiteral(token.token_value)

        if token.token_type == constant.TokenType.PAREN and token.token_value == "(":
            self.current_idx += 1
            token = self.get_token()

            node = constant.CallExpression(token.token_value)
            self.current_idx += 1
            token = self.get_token()

            while token.token_type != constant.TokenType.PAREN or \
                    (token.token_type == constant.TokenType.PAREN and token.token_value != ")"):
                node.params.append(self.walk_tokens())
                token = self.get_token()

            self.current_idx += 1
            return node

        raise InvalidTokenTypeFoundExeception(
            f"The self.tokens contains an unexpected token: {self.tokens[self.current_idx]}"
        )

    def get_token(self) -> 'Token':
        """Function to get the current token.

        Returns:
            Token: An instance of Token class
        Raises:
            ParserIndexExeception: Raised when the index is out of range
        """
        if len(self.tokens) <= self.current_idx:
            raise ParserIndexExeception(
                f"The current index '{self.current_idx}' is out of range"
            )

        return self.tokens[self.current_idx]
