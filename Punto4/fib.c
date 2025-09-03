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
