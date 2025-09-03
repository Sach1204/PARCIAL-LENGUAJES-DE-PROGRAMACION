import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 40  # mismo número
start = time.time()

resultado = fib(n)

end = time.time()
print(f"Fib({n}) = {resultado}")
print(f"Tiempo en Python: {end - start:.6f} segundos")
