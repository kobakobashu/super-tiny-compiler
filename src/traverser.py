from typing import Callable, List, Optional

from src import constant


class Traverser:
    def __init__(self, ast: constant.Program) -> None:
        """Inits Traverser.

        Args:
            ast: An instance of Program which means Abstract Syntax Tree
        """
        self.ast = ast

    def traverse(self) -> None:
        """Function to traverse self.ast.

        This method calls traverse_node to do a recursive depth-first search in ast.
        """
        self.traverse_node(self.ast)

    def traverse_array(self, node_array: List[constant.Node], parent: constant.Node) -> None:
        """Function to itelate the ast elements.

        Args:
            node_array: A node list whose elements have same parent node
            parent: A parent node
        """
        for child in node_array:
            self.traverse_node(child, parent)

    def traverse_node(self, node: constant.Node, parent: constant.Node = None) -> None:
        """Function to traverse node by depth-first search.

        Args:
            node: A child node
            parent: A parent node
        Raises:
            InvalidNodeTypeFoundExeception: Raised when the ast contains unexpected NodeType
        """
        visitor = {
            constant.NodeType.NUMBER_LITERAL: ContextHundler(constant.NodeType.NUMBER_LITERAL),
            constant.NodeType.STRING_LITERAL: ContextHundler(constant.NodeType.STRING_LITERAL),
            constant.NodeType.CALL_EXPRESSION: ContextHundler(constant.NodeType.CALL_EXPRESSION),
        }
        methods = visitor.get(node.type)

        if methods and methods.enter:
            methods.enter(node, parent)

        if node.type == constant.NodeType.PROGRAM:
            self.traverse_array(node.body, node)
        elif node.type == constant.NodeType.CALL_EXPRESSION:
            self.traverse_array(node.params, node)
        elif node.type == constant.NodeType.NUMBER_LITERAL:
            pass
        elif node.type == constant.NodeType.STRING_LITERAL:
            pass


class ContextHundler:
    def __init__(self, node_type: 'constant.NodeType') -> None:
        """Inits ContextHundler.

        Args:
            node_type: A constant string which means node type defined in NodeType
        """
        self.enter = self.define_enter(node_type)

    def define_enter(self, node_type: 'constant.NodeType') -> Callable[[constant.Node, Optional[constant.Node]], None]:
        """Function to call the corresponding method.

        Args:
            node_type: A constant string which means node type defined in NodeType
        Returns:
            Callable: The corresponding method object
        """
        if node_type == constant.NodeType.NUMBER_LITERAL:
            return self.number_literal_enter
        if node_type == constant.NodeType.STRING_LITERAL:
            return self.string_literal_enter
        if node_type == constant.NodeType.CALL_EXPRESSION:
            return self.call_expression_enter

    def number_literal_enter(self, node: constant.NumberLiteral, parent: constant.Node) -> None:
        """Function to process the node when number literal node is searched.

        Args:
            node: A child NumberLiteral node
            parent: A parent node
        """
        parent.context.append(constant.NumberLiteral(node.value))

    def string_literal_enter(self, node: constant.StringLiteral, parent: constant.Node) -> None:
        """Function to process the node when string literal node is searched.

        Args:
            node: A child StringLiteral node
            parent: A parent node
        Returns:
            Callable: The corresponding method object
        """
        parent.context.append(constant.StringLiteral(node.value))

    def call_expression_enter(self, node: constant.CallExpression, parent: constant.Node) -> None:
        """Function to process the node when call expression node is searched.

        Args:
            node: A child CallExpression node
            parent: A parent node
        Returns:
            Callable: The corresponding method object
        """
        expression = constant.CallExpressionWithCallee(node.value)
        node.context = expression.arguments

        if parent.type != constant.NodeType.CALL_EXPRESSION:
            expression = constant.ExpressionStatement(expression)
            node.context = expression.expression.arguments

        parent.context.append(expression)
