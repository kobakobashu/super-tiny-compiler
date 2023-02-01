from src import constant
from src.traverser import Traverser


class Transformer:
    def __init__(self, ast: constant.Program) -> None:
        """Inits Transformer.

        Args:
            ast: An instance of Program which means Abstract Syntax Tree
        """
        self.ast = ast

    def transform(self) -> constant.TransformedProgram:
        """Function to transforme self.ast.

        Returns:
            constant.TransformedProgram: A transformed ast.
            Example:
                TransformedProgram(
                    type: 'Program',
                    body:[
                        type: 'ExpressionStatement',
                        expression: CallExpression(
                            type: 'CallExpression'
                            callee: ...
                        )
                    ]
                )
        """
        transformed_ast = constant.TransformedProgram()
        self.ast.context = transformed_ast.body
        Traverser(self.ast).traverse()

        return transformed_ast
