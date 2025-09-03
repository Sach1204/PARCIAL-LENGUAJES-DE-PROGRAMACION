## PUNTO 5
Escriba un programa en ANTLR que pueda calcular la secuencia de Fibonacci de un numero dado. La forma de calcular el Fibonacci debe ser: FIBO(20) y debe retornar: 0, 1, 1, 2, 3, 5, 8, 13. La entrada y la salida debe ser 
por consola. El lenguaje objetivo debe ser Python

### Gramatica en ANTLR (Fibo.g4)
```antlr
grammar Fibo;

prog : 'FIBO' '(' NUM ')' EOF ;

NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;

```
### Paso para generar el codigo en PYTHON
```bash
antlr4 -Dlanguage=Python3 Fibo.g4
```
### Codigo en Python del Visitor (FiboVisitorImpl.py)
```python
from FiboVisitor import FiboVisitor

# Función recursiva de Fibonacci
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

class FiboVisitorImpl(FiboVisitor):
    def visitProg(self, ctx):
        n = int(ctx.NUM().getText())
        secuencia = [str(fibo(i)) for i in range(n)]
        print(", ".join(secuencia))
        return secuencia

```
### Codigo en Python principal (main.py)
```python
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

```


### Salida en Terminal 
