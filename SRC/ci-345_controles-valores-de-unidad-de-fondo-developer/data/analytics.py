'''Se definen las funciones que nos permiten hacer un estudio de los datos '''
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import shapiro

def analisis(data):
    '''Esta funcion nos permite visualizar el comportamiento de los datos
    con histograma, diagrama de caja y diagrama Q-Q'''
    fig, axs = plt.subplots(nrows=1, ncols=3,figsize=(25,10))
    sns.histplot(data['f0_'],ax=axs[0])
    axs[0].set_title('densidad')
    sns.boxplot(data = data, y = 'f0_', ax=axs[1])
    axs[1].set_title('Diagrama de bigotes')
    stats.probplot(data['f0_'],dist='norm',plot=plt)
    axs[2].set_title('Q-Q')
    return plt.show()

def historic(data):
    '''Esta funcion nos permiten visualizar el historico de los datos'''
    plt.figure()
    sns.lineplot(x='ds', y='CAMBIO', data= data)
    plt.legend(data['NEMOTECNICO'].iloc[:])
    return plt.show()

def rename(data):
    '''Con esta funcion cambiamos los nombres de las columnas del dataframe para ingresarlos a prophet'''
    new_column_names = {'FECHA_VALORACION':'ds'} 
    data.rename(columns=new_column_names, inplace=True)
    df = data.copy()
    new_column_names = {'f0_':'y'}
    df.rename(columns=new_column_names, inplace=True)
    df.sort_values(by='ds')
    return df

def prueba_shapiro(data):
    '''Esta funcion utiliza la prueba shapiro para identificar si los datos siguen una distribucion normal'''
    stat, p = shapiro(data['f0_'])
    print('stat=%.5f, p=%.5f' % (stat,p))
    alpha = 0.05
    if p > alpha:
        return f'los datos parecen normales para el nemotecnico {data["NEMOTECNICO"].iloc[0]} (no se puede rechazar H0)'
    else:
        return f'Los datos no parecen normales para el nemotecnico {data["NEMOTECNICO"].iloc[0]} (se rechaza H0)'