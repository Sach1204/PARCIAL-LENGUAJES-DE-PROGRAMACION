1. Para el siguiente ejercicio, de una expresión regular que represente el conjunto descrito. [El conjunto de cadenas sobre {**a**,**b**, **c**} en el cual todas las **a** preceden a las **b** y 
éstas a su vez preceden a las **c**. Es posible que no haya **a**, **b** o **c**]. Implemente el AFD para esta expresión 
regular. Use Python.

**Codigo para la Configuración del Automata (Configuracion.txt)**
```txt
# Estados
q0,q1,q2,qE
# Alfabeto
a,b,c
# Estado inicial
q0
# Estados de aceptación
q0,q1,q2
# Transiciones (origen, simbolo, destino)
q0,a,q0
q0,b,q1
q0,c,q2
q1,b,q1
q1,c,q2
q1,a,qE
q2,c,q2
q2,a,qE
q2,b,qE
qE,a,qE
qE,b,qE
qE,c,qE

```
**TXT con las Pruebas que va a tener el Automata (Cadenas.txt)**
```txt
aaabbcc
bbb
c
acb
abc
```
**Codigo en Python del AFD (a,b,c)**
```python
def cargar_configuracion(archivo_configuracion):
    with open(archivo_configuracion, 'r') as f:
        lineas = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    estados = lineas[0].split(',')
    alfabeto = lineas[1].split(',')
    estado_inicial = lineas[2]
    estados_aceptacion = lineas[3].split(',')
    
    transiciones = {}
    for linea in lineas[4:]:
        origen, simbolo, destino = linea.split(',')
        transiciones[(origen, simbolo)] = destino

    return estados, alfabeto, estado_inicial, estados_aceptacion, transiciones


def evaluar_cadena(cadena, estado_inicial, estados_aceptacion, transiciones):
    # 🔹 Caso especial: cadena vacía => NO ACEPTA
    if cadena == "":
        return False

    estado_actual = estado_inicial
    for simbolo in cadena:
        if (estado_actual, simbolo) in transiciones:
            estado_actual = transiciones[(estado_actual, simbolo)]
        else:
            return False
    return estado_actual in estados_aceptacion


def main():
    estados, alfabeto, estado_inicial, estados_aceptacion, transiciones = cargar_configuracion('Configuracion.txt')
    
    with open('Cadenas.txt', 'r') as f:
        cadenas = [line.strip() for line in f if line.strip() or line == ""] 
    
    for cadena in cadenas:
        resultado = "ACEPTA" if evaluar_cadena(cadena, estado_inicial, estados_aceptacion, transiciones) else "NO ACEPTA"
        # Mostrar explícitamente la cadena vacía como "" para que se vea
        cadena_mostrar = cadena if cadena != "" else '"" (cadena vacía)'
        print(f"{cadena_mostrar}: {resultado}")


if __name__ == "__main__":
    main()
```
