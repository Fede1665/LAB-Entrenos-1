from typing import NamedTuple
from datetime import datetime
import csv

Entreno = NamedTuple('Entreno', 
    [('tipo',str),('fechahora', datetime),('ubicacion', str), ('duracion', int), ('calorias', int), ('distancia', float),('frecuencia', int), ('compartido', bool)])


def lee_entrenos(ruta):
    lista_entrenos=[]
    with open(ruta, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            tipo=str(tipo)
            fechahora=datetime.strptime(fechahora,'%d/%m/%Y %H:%M')
            ubicacion= str(ubicacion)
            duracion= int (duracion)
            calorias= int (calorias)
            distancia= float (distancia)
            frecuencia= int (frecuencia)
            compartido = compartido == "s"
            r=Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            lista_entrenos.append(r)
    return lista_entrenos

def tipos_entrenos(lista_entrenos: list[Entreno]) -> list[str]:
    tipos= set()
    for entreno in lista_entrenos:
        tipos.add(entreno.tipo)
    return sorted(tipos)

