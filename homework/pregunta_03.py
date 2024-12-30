"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("files/input/tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """

    return tbl0.groupby('c1')['c1'].count()

#print(pregunta_03())