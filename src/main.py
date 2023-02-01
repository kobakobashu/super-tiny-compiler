from src.code_generator import CodeGenerator
from src.parser import Parser
from src.tokenizer import Tokenizer
from src.transformer import Transformer


def compiler(input):
    tokens = Tokenizer(input).tokenize()
    ast = Parser(tokens).parse()
    new_ast = Transformer(ast).transform()
    output = CodeGenerator(new_ast).generate_code()
    print(output)


if __name__ == "__main__":
    compiler("()")
    compiler("(add 2 (subtract 4 2))")
    compiler("(add -1 4)")
