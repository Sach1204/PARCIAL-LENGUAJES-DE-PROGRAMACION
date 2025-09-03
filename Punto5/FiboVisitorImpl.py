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
