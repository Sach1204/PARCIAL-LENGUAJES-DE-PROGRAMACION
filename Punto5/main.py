from antlr4 import *
from FiboLexer import FiboLexer
from FiboParser import FiboParser
from FiboVisitorImpl import FiboVisitorImpl

def main():
    # Leer la instrucción desde consola
    entrada = InputStream(input("Ingresa la instrucción (ej: FIBO(8)): "))

    lexer = FiboLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = FiboParser(tokens)
    tree = parser.prog()

    visitor = FiboVisitorImpl()
    visitor.visit(tree)

if __name__ == "__main__":
    main()
