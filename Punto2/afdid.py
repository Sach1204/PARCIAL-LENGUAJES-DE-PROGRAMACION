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
    estados, alfabeto, estado_inicial, estados_aceptacion, transiciones = cargar_configuracion('ConfiguracionId.txt')

    with open('CadenasId.txt', 'r') as f:
        cadenas = [line.rstrip("\n") for line in f]

    for cadena in cadenas:
        if cadena == "":
            print('"" (cadena vacía): NO ACEPTA')
        else:
            resultado = "ACEPTA" if evaluar_cadena(cadena, estado_inicial, estados_aceptacion, transiciones) else "NO ACEPTA"
            print(resultado)


if __name__ == "__main__":
    main()
