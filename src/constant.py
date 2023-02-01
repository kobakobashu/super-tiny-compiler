from enum import Enum


class TokenType(Enum):
    NUMBER = "number"
    STRING = "string"
    NAME = "name"
    PAREN = "paren"


class NodeType(Enum):
    PROGRAM = "Program"
    CALL_EXPRESSION = "CallExpression"
    NUMBER_LITERAL = "NumberLiteral"
    STRING_LITERAL = "StringLiteral"
    EXPRESSION_STATEMENT = "ExpressionStatement"
    IDENTIFIER = "Identifier"


class Node(Enum):
    pass


class TraversedNode(Enum):
    pass


class NumberLiteral:
    def __init__(self, value: str):
        self.type = NodeType.NUMBER_LITERAL
        self.value = value
        self.context = []

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value and self.context == other.context


class StringLiteral:
    def __init__(self, value):
        self.type = NodeType.STRING_LITERAL
        self.value = value
        self.context = []

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value and self.context == other.context


class CallExpression:
    def __init__(self, value):
        self.type = NodeType.CALL_EXPRESSION
        self.value = value
        self.params = []
        self.context = []

    def __eq__(self, other):
        return (self.type == other.type and self.value == other.value and 
                self.params == other.params and self.context == other.context)


class Program:
    def __init__(self):
        self.type = NodeType.PROGRAM
        self.body = []
        self.context = []
    
    def __eq__(self, other):
        return self.type == other.type and self.body == other.body and self.context == other.context


class TransformedProgram:
    def __init__(self) -> None:
        self.type = NodeType.PROGRAM
        self.body = []

    def __eq__(self, other):
        return self.type == other.type and self.body == other.body

class ExpressionStatement:
    def __init__(self, expression):
        self.type = NodeType.EXPRESSION_STATEMENT
        self.expression = CallExpressionWithCallee(expression.callee.name)

    def __eq__(self, other):
        return self.type == other.type and self.expression == other.expression


class CallExpressionWithCallee:
    def __init__(self, name):
        self.type = NodeType.CALL_EXPRESSION
        self.callee = Identifier(name)
        self.arguments = []

    def __eq__(self, other):
        return self.type == other.type and self.callee == other.callee and self.arguments == other.arguments


class Identifier:
    def __init__(self, name):
        self.type = NodeType.IDENTIFIER
        self.name = name

    def __eq__(self, other):
        return self.type == other.type and self.name == other.name


"""class Hundler:
    def __init__(self, node_type) -> None:
        self.enter = self.define_enter(node_type=node_type)
        self.exit = self.define_exit(node_type=node_type)

    def define_enter(self, node_type):
        if node_type == NodeType.PROGRAM:
            return self.program_enter
        if node_type == NodeType.CALL_EXPRESSION:
            return self.call_expression_enter
        if node_type == NodeType.NUMBER_LITERAL:
            return self.number_literal_enter
        if node_type == NodeType.STRING_LITERAL:
            return self.string_literal_enter

    def define_exit(self, node_type):
        if node_type == NodeType.PROGRAM:
            return self.program_exit
        if node_type == NodeType.CALL_EXPRESSION:
            return self.call_expression_exit
        if node_type == NodeType.NUMBER_LITERAL:
            return self.number_literal_exit
        if node_type == NodeType.STRING_LITERAL:
            return self.string_literal_exit

    def program_enter(self, node, parent):
        print(f'enter node: {node}, parent: {parent}')

    def call_expression_enter(self, node, parent):
        print(f'enter node: {node}, parent: {parent}')

    def number_literal_enter(self, node, parent):
        print(f'enter node: {node}, parent: {parent}')

    def string_literal_enter(self, node, parent):
        print(f'enter node: {node}, parent: {parent}')


    def program_exit(self, node, parent):
        print(f'exit node: {node}, parent: {parent}')

    def call_expression_exit(self, node, parent):
        print(f'exit node: {node}, parent: {parent}')

    def number_literal_exit(self, node, parent):
        print(f'exit node: {node}, parent: {parent}')

    def string_literal_exit(self, node, parent):
        print(f'exit node: {node}, parent: {parent}')"""