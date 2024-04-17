from dotenv import load_dotenv
from google.cloud import bigquery
import os
import sys
import pandas as pd

src_path = os.path.join(os.path.dirname(os.getcwd()), 'src')
sys.path.append(src_path)

def bq_consulta(sql):
    """
    función para hacer consulta de bigquery
    Parameters:
        sql (str): query para ejecutar consulta
    Returns:
        df (pandas.DataFrame): Tabla con los datos de la consulta.
    """

    client = bigquery.Client()
    df = client.query(sql).to_dataframe()
    return df

def charge_data():
    '''Con esta funcion leemos las variables de entorno y accedemos a la base de datos de BigQuery'''
    load_dotenv()
    PROJECT = os.getenv('PROJECT')
    DATASET = os.getenv('DATASET')
    sql_text = f"""SELECT FECHA_VALORACION,NEMOTECNICO, AVG(VALOR_UTILIDAD_PERDIDA / valor_mercado) 
    FROM `{PROJECT}.{DATASET}.SQLSERVER_SPIRITDB_SPIRIT_TSPT_VALORACION_POS` WHERE VALOR_MERCADO != 0 AND NEMOTECNICO IS NOT NULL GROUP BY FECHA_VALORACION, NEMOTECNICO"""
    data = bq_consulta(sql_text)
    return data

def modify_data(NEMOTECNICO:str):
    '''Con esta funcion se cambia el formato con el que vienen los datos por defecto'''
    df =  charge_data()
    df['FECHA_VALORACION'] = pd.to_datetime(df['FECHA_VALORACION'], dayfirst=True)
    datos = df.loc[df['NEMOTECNICO'] == NEMOTECNICO]
    return datos

