# informe.py
import fileparse
from lote import Lote
from camion import Camion
import formato_tabla

def leer_camion(filename):
    '''
    Lee un archivo con el contenido de un camión 
    y lo devuelve como un objeto Camion.
    '''
    with open(filename) as file:
        camiondicts = fileparse.parse_csv(file,
                                        select=['nombre','cajones','precio'],
                                        types=[str,int,float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)

#%%
    
def leer_precios(nom_archivo):
    '''
    Lee un archivo CSV con data de precios
    y lo devuelve como un diccionario
    con claves nombres y con sus precios como valores
    '''
    with open(nom_archivo) as lines:
        return dict(fileparse.parse_csv(lines, types = [str,float], 
                                        has_headers = False))
#%%
def hacer_informe(camion, precios):
    '''
    Crea una lista de tuplas (nombre, cajones, precio, cambio)
    dada una lista de lotes en un camión y un diccionario de precios nuevos.
    '''
    filas = []
    for c in camion:
        precio_orig = c.precio
        cambio = precios[c.nombre] - precio_orig
        reg = (c.nombre, c.cajones, precio_orig, cambio)
        filas.append(reg)
    return filas
#%%
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia)
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)
#%%
def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)
    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
#%%
def main(args):
    if len(args) == 3:        
        informe_camion(args[1], args[2])
    elif len(args) == 4:
        informe_camion(args[1], args[2], fmt = args[3])
    else:
        raise SystemExit('Uso: %s archivo_camion archivo_precios formato' % args[0])
#%%
if __name__ == '__main__':
    import sys
    main(sys.argv)
    
