
import os
import pickle 
import pandas as pd

archivos = os.listdir('/home/aescobag@PROTECCION.LOCAL/ci-345_controles-valores-de-unidad-de-fondo/src/ci-345_controles-valores-de-unidad-de-fondo/modelos/modelos_entrenados')


modelo_g= open(f'/home/aescobag@PROTECCION.LOCAL/ci-345_controles-valores-de-unidad-de-fondo/src/ci-345_controles-valores-de-unidad-de-fondo/modelos/modelos_entrenados/modelo_TUVT10180429.pkl', 'rb')
modelo_c = pickle.load(modelo_g)

print(modelo_c.predict())