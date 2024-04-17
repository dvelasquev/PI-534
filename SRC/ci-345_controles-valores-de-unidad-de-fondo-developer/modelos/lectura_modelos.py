
import os
import pickle 
import pandas as pd

archivos = os.listdir('/home/aescobag@PROTECCION.LOCAL/ci-345_controles-valores-de-unidad-de-fondo/src/ci-345_controles-valores-de-unidad-de-fondo/modelos/modelos_entrenados')

def obtener_modelo():
    """
    Con esta funcion se obtienen los modelos almacenados con pickle para su uso
    Se elimina la parte modelo_ .pkl de los nombres de los archivos y se guardar el modelo correspondiente

    """

    diccionario_modelos = {}
    for archivo in archivos:
        try:
            modelo_g= open(f'/home/aescobag@PROTECCION.LOCAL/ci-345_controles-valores-de-unidad-de-fondo/src/ci-345_controles-valores-de-unidad-de-fondo/modelos/modelos_entrenados/{archivo}', 'rb')
            modelo_c = pickle.load(modelo_g)
            archiv = archivo[7:].split('_')
            diccionario_modelos[f'{archiv[0][:-4]}'] = modelo_c
        except Exception: 
            pass
    return diccionario_modelos

def obtener_columnas():
    'Esta funcion permite obtener las columnas de la base de datos para marcar las clases de inversiones en modelo.py'
    
    d = open(f'/home/aescobag@PROTECCION.LOCAL/ci-345_controles-valores-de-unidad-de-fondo/src/ci-345_controles-valores-de-unidad-de-fondo/modelos/modelos_entrenados/data.pkl', 'rb') 
    data = pickle.load(d)
    return data.columns

if __name__ == "__main__":
    print(obtener_columnas())