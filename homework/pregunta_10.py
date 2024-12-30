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

def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """

    df = tbl0.groupby('c1')['c2'].apply(lambda x: sorted(list(x))).reset_index()
    df['c2'] = df['c2'].apply(lambda x: ':'.join([str(e) for e in x]))
    df.set_index('c1', inplace=True)
    return df

#print(pregunta_10())