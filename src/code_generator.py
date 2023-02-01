from src import constant


class InvalidTraversedNodeTypeFoundExeception(Exception):
    """Raised when the traversed ast contains unexpected NodeType."""
    pass


class CodeGenerator:
    def __init__(self, node: constant.TransformedProgram) -> None:
        """Inits CodeGenerator.

        Args:
            node: An instance of TransformedProgram which means transformed Abstract Syntax Tree
        """
        self.node = node

    def generate_code(self) -> str:
        """Function to call generate_code method to generate code.

        Returns:
            str: A compiled string
        """
        return self.generate_code_recursively(self.node)

    def generate_code_recursively(self, node: constant.TraversedNode) -> str:
        """Function to generate code by depth-first search.

        Args:
            node: A traversed node
        Raises:
            InvalidNodeTypeFoundExeception: Raised when the ast contains unexpected NodeType
        """
        if node.type == constant.NodeType.PROGRAM:
            return "\n".join(map(self.generate_code_recursively, node.body))

        elif node.type == constant.NodeType.EXPRESSION_STATEMENT:
            return self.generate_code_recursively(node.expression) + ";"

        elif node.type == constant.NodeType.CALL_EXPRESSION:
            return self.generate_code_recursively(node.callee) + "(" + ", ".join(map(self.generate_code_recursively, node.arguments)) + ")"

        elif node.type == constant.NodeType.IDENTIFIER:
            return node.name

        elif node.type == constant.NodeType.NUMBER_LITERAL:
            return node.value

        elif node.type == constant.NodeType.STRING_LITERAL:
            return '"' + node.value + '"'

        else:
            raise InvalidTraversedNodeTypeFoundExeception(
                f"The traversed ast contains an unexpected node type: {node.type}"
            )
