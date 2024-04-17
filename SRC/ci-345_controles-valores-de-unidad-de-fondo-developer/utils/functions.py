import pandas as pd
import pickle

def lanzar_alerta(fecha:str, NEMOTECNICO:str, valor_unidad):
    datos = pd.DataFrame([[fecha,NEMOTECNICO,valor_unidad]], columns = ['Fecha','NEMOTECNICO', 'valor_unidad'])
    datos['Fecha'] = pd.to_datetime(datos['Fecha'], dayfirst=True)
    nombre_archivo = f'modelo_{NEMOTECNICO}.pkl'
    modelo= open(f'notebooks/modelos/{nombre_archivo}', 'rb')
    modelo_cargado = pickle.load(modelo)
    resultado = modelo_cargado.predict(datos['valor_unidad'].to_numpy().reshape(-1,1))
    return resultado