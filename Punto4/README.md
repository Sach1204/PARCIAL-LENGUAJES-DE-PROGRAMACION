# PUNTO 4
Realice la comparación del rendimiento de un lenguaje de programación compilado y un lenguaje de programación interpretado. Utilice la función recursiva para la 
comparación.

## Solucion

Para poder ver la comparacion de un lenguaje de progrmacion compilado y un lenguaje Interpretado, realice en **C** y en **Python** el mismo codigo el cual realiza la sucesion de Fibonacci de manera recursiva con el mismo numero
lo unico extra que se le añadio a ambos codigo fue la Libreria de tiempo para poder medir cual es mas rapido que el otro.

### Codigo en Python
```python
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

```
### Codigo en C
```c
#include <stdio.h>
#include <time.h>

// Función recursiva de Fibonacci
long long fib(int n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}

int main() {
    int n = 40; // número a calcular
    clock_t start = clock();

    long long resultado = fib(n);

    clock_t end = clock();
    double tiempo = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Fib(%d) = %lld\n", n, resultado);
    printf("Tiempo en C: %f segundos\n", tiempo);
    return 0;
}

```
### Salida en Terminal de Ambos Codigos con tiempo de Ejecución

### Conclusiones

C es mucho más rápido al estar compilado, mientras que Python al ser interpretado tarda bastante más en mostrar el resultado.
