**PUNTO 2**

<img width="662" height="119" alt="image" src="https://github.com/user-attachments/assets/8be3141d-f3df-4867-af89-6176e803d2ce" />

**Codigo para la Configuración del Automata (ConfiguracionId.txt)**
```txt
# Estados
q0,q1,qE
# Alfabeto
a-z,A-Z,0-9
# Estado inicial
q0
# Estados de aceptación
q1
# Transiciones (origen, simbolo, destino)
q0,letra,q1
q0,digito,qE
q1,letra,q1
q1,digito,q1
qE,letra,qE
qE,digito,qE

```
**TXT con las Pruebas que va a tener el Automata (CadenasId.txt)**
```txt
abc123
ID9
x
9inicio
hola-mundo

```
**Codigo en Python del AFD del ID**
```python
def es_letra(ch):
    return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')

def es_digito(ch):
    return '0' <= ch <= '9'

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
    if cadena == "":   # caso cadena vacía
        return False

    estado_actual = estado_inicial

    for i, simbolo in enumerate(cadena):
        # Determinar si es letra o dígito
        if es_letra(simbolo):
            tipo = "letra"
        elif es_digito(simbolo):
            tipo = "digito"
        else:
            return False  # cualquier otro carácter no se acepta

        # Consultar transición
        if (estado_actual, tipo) in transiciones:
            estado_actual = transiciones[(estado_actual, tipo)]
        else:
            return False

    return estado_actual in estados_aceptacion


def main():
    estados, alfabeto, estado_inicial, estados_aceptacion, transiciones = cargar_configuracion('Configuracion.txt')

    with open('Cadenas.txt', 'r') as f:
        cadenas = [line.rstrip("\n") for line in f]

    for cadena in cadenas:
        if cadena == "":
            print('"" (cadena vacía): NO ACEPTA')
        else:
            resultado = "ACEPTA" if evaluar_cadena(cadena, estado_inicial, estados_aceptacion, transiciones) else "NO ACEPTA"
            print(resultado)


if __name__ == "__main__":
    main()

```
**Como sale por Terminal el codigo ejecutado**
