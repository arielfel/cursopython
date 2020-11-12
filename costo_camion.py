#costo_camion_2.19.py modificado por 5.9, 6.2 y 6.3
import csv
from informe_funciones import leer_camion
def costo_camion(nombre_archivo):
    record = leer_camion(nombre_archivo)
    costo_total = 0
    for i, fila in enumerate(record):
        try:
            ncajones = record[i]['cajones']
            precio = record[i]['precio']
            costo_total += ncajones * precio
        except ValueError:
            print(f'La línea {i} tiene datos no válidos.')
    return costo_total
def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Uso adecuado: {argv[0]} ' 'archivo_camion')
    camion = argv[1]
    print(f'Costo total: {costo_camion(camion)}')
if __name__ == '__main__':
    import sys
    main(sys.argv)
