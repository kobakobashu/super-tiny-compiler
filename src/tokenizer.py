import re
from typing import List

from src.constant import TokenType


class CloseQuoteNotFoundExeception(Exception):
    """Raised when there are no close quotes in the input string."""
    pass


class TokenizerIndexExeception(Exception):
    """Raised when the index is out of range."""
    pass


class InvalidInputFoundExeception(Exception):
    """Raised when the input contains unexpected characters."""
    pass


class Token:
    def __init__(self, token_type: 'TokenType', token_value: str) -> None:
        """Inits Token.

        Args:
            token_type: A TokenType which means the token type. It is defined as Enum
            token_value: A string such as "add", "2", and "("
        """
        self.token_type = token_type
        self.token_value = token_value
    
    def __eq__(self, other):
        return self.token_type == other.token_type and self.token_value == other.token_value


class Tokenizer:
    def __init__(self, input: str) -> None:
        """Inits Token.

        Args:
            input: A string which is tokenized such as "(add 2 (subtract 4  2))"
        """
        self.input = input
        self.current_idx = 0
        self.tokens = []

    def tokenize(self) -> List['Token']:
        """Function to tokenize the string self.input.

        This method looks at the input characters one at a time and tokenize them.

        Returns:
            list['Token']: A list of Token like [class Token(type: 'paren', value: '('), ...]
        Raises:
            InvalidInputFoundExeception: Raised when the input contains unexpected characters
        """
        while self.current_idx < len(self.input):
            WHITESPACE = "\s|\r\n|\n|\r"
            if re.match(WHITESPACE, self.get_char()):
                while self.current_idx < len(self.input) and re.match(WHITESPACE, self.get_char()):
                    self.current_idx += 1
                continue

            if self.get_char() in ["(", ")"]:
                self.tokens.append(Token(TokenType.PAREN, self.get_char()))
                self.current_idx += 1
                continue

            token_value = ""
            NUMBERS = "[0-9]"
            if self.get_char() == "-":
                token_value += self.get_char()
                self.current_idx += 1
                if re.match(NUMBERS, self.get_char()):
                    while self.current_idx < len(self.input) and re.match(NUMBERS, self.get_char()):
                        token_value += self.get_char()
                        self.current_idx += 1
                    self.tokens.append(Token(TokenType.NUMBER, token_value))
                else:
                    raise InvalidInputFoundExeception(
                        f"The input contains an unexpected character: {self.input[self.current_idx]}"
                    )
                continue

            if re.match(NUMBERS, self.get_char()):
                while self.current_idx < len(self.input) and re.match(NUMBERS, self.get_char()):
                    token_value += self.get_char()
                    self.current_idx += 1
                self.tokens.append(Token(TokenType.NUMBER, token_value))
                continue

            QUOTES = "['\"]"
            if re.match(QUOTES, self.get_char()):
                self.current_idx += 1
                while not re.match(QUOTES, self.get_char()):
                    token_value += self.get_char()
                    self.current_idx += 1
                    if self.current_idx == len(self.input):
                        raise CloseQuoteNotFoundExeception(
                            f"There are no close quotes in the input string"
                        )

                self.current_idx += 1
                self.tokens.append(Token(TokenType.STRING, token_value))
                continue

            LETTERS = "[a-zA-Z_-]"
            if re.match(LETTERS, self.get_char()):
                while self.current_idx < len(self.input) and re.match(LETTERS, self.get_char()):
                    token_value += self.get_char()
                    self.current_idx += 1

                self.tokens.append(Token(TokenType.NAME, token_value))
                continue

            raise InvalidInputFoundExeception(
                f"The input contains an unexpected character: {self.input[self.current_idx]}"
            )

        return self.tokens

    def get_char(self) -> str:
        """Function to get the current index character.

        Returns:
            str: A character specified by self.current_idx
        Raises:
            TokenizerIndexExeception: Raised when the index is out of range
        """
        if len(self.input) <= self.current_idx:
            raise TokenizerIndexExeception(
                f"The current index '{self.current_idx}' is out of range"
            )

        return self.input[self.current_idx]
