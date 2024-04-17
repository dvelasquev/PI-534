
import pandas as pd
import sys
sys.path.append('src/ci-345_controles-valores-de-unidad-de-fondo')

from modelos.lectura_modelos import obtener_modelo
from modelos.lectura_modelos import obtener_columnas

class IF:
    """
    Clase que permite modificar los datos obtenidos desde la API para generar la alerta

    """
    
    def __init__(self):
        self.modelos = obtener_modelo()
    
    def completar_columnas(self, fecha):
        """
        Función que calcula los días transcurridos, necesarios para ingresarlos al modelo

        Args: 
        fecha: str con la fecha en formato AA-MM-DD

        Results: 
        dias: dias transcurridos desde la fecha minima de los datos tomados y el dia ingresado

        """

        dias = (pd.to_datetime(fecha) - pd.to_datetime('2017-11-16')).days
        return dias

    def transformar_datos(self, fecha:str,NEMOTECNICO:str, cambio_valoracion,clase_inversion:str,pago):
        """
        Funcion que crea el dataframe para ingresar al modelo 

        1. Se transforma en un dataframe los datos ingresados 
        2. Se crean columnas adicionales para cubrir el one hot encoding del entrenamiento (se añade 1 según el tipo de inversión) 
        3. Se eliminan las columnas de tipo string 
        
        """

        dias = self.completar_columnas(fecha)
        datos = pd.DataFrame([[dias]], columns = ['dias'])
        datos['CAMBIO'] = cambio_valoracion

        for i in obtener_columnas():
            nombre_columna = i.replace('CLASE_INVERSION_','')
            if clase_inversion == nombre_columna:
                datos[i] = 1
            elif clase_inversion != nombre_columna and nombre_columna != 'CAMBIO':
                datos[i] = 0

        datos = datos.drop(columns = ['FECHA_ANTERIOR','MAX_DATE','INTERESES','VALOR_NOMINAL_OP','PRECIO','ANTERIOR','FECHA_VALORACION','NEMOTECNICO'])
        datos['PAGO'] = pago

        return datos

    
    def generar_alerta(self,fecha,nombre_modelo:str, cambio_valoracion,clase_inversion:str, pago):
        """
        Esta funcion genera las alertas de si la valoracion del portafolio es atipica o es normal 

        Args: 

        fecha: fecha de valoracion del portafolio
        nombre_modelo: nombre del nemotecnico 
        clase_inversion: codigo de la clase de inversion
        pago: si hubo abonos debe ser 0 si no hubo, 1 si hubo 

        Results: 

        Alerta: se genera alerta cuando el dato es atipico ( -1 arrojado por el modelo )

        """
        array_training = self.transformar_datos(fecha,nombre_modelo,cambio_valoracion,clase_inversion, pago)
        if nombre_modelo in self.modelos:
            modelo = self.modelos[nombre_modelo]
            resultado = modelo.predict(array_training.to_numpy())
        return ('El dato no parece ser atipico' if resultado == 1 else 'Revisar')
    
if __name__ == "__main__":   
    """
    Pruebas:
    En esta nueva version con covariables se está enviando -1 para datos que en el entrenamiento en el notebook tienen salida 1
    Archivos implicados: modelo.py - lectura_modelos.py
    Los anteriores archivos son los que deben ser modificados para obtener resultados coherentes
    
    """
    IsoF = IF()
    print(IsoF.transformar_datos('2020-06-05','TUVT10180429',0.000117,'TSUV',0))
    print(IsoF.generar_alerta('2020-06-05','TUVT10180429',0.000000117,'TSUV',0))

    