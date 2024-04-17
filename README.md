# Readme del proyecto ci-345_controles-valores-de-unidad-de-fondo
El objetivo es la intervención del proceso de control a la valoración de las unidades de fondos  enfocado en la generación de las alertas de datos atipicos en los portafolios de inversion

## 1. Subproceso
Nombre del subproceso del cual hace parte el desarrollo que se está trabajando

## 2. Objetivo
Detectar anomalias en la valoracion de los portafolios de inversión

## 3. Alcance
Se hizo una primera versión (api_funcional en el repo) analizando los cambios en la valoración
La ultima version V2 esta alimentada con covariables adicionales y con una nueva consulta en sql de las valoraciones 
de los portafolios, en el entrenamiento los datos funcionan correctamente, al modificar la API en la nueva version
 en modelo.py se genera cualquier valor como atipico esto debe revisarse para evitar valores falsos 

## 4. Periodicidad 
Diariamente desde tesoreria se ingresan los datos

## 5. Responsable y Líder:
Daniel Betancur Rodriguez 

## 6. Ruta(s) de GIT 
https://vostpmde37.proteccion.com.co:10443/analitica/tesoreria/ci-345_controles-valores-de-unidad-de-fondo

## 7. Fuentes 
`sura-inception.proteccion_co_zcarga_inversiones.SQLSERVER_SPIRITDB_SPIRIT_TSPT_VALORACION_POS`
`sura-inception.proteccion_co_zcarga_inversiones.SQLSERVER_SPIRITDB_SPIRIT_TSPT_VENCIMIENTOS`

## 8. Salidas 
- Llamado de api: actualmente probando en local

## 9. Diagrama del proceso 



## 10. Pruebas 


## 11. Beneficios
Se ahorra tiempo y dinero debido a que el proyecto funciona como revision de la valoracion de los portafolios, ayuda a brindar mayor seguridad sobre esta valoracion y
ayuda a prevenir el pago de resarcimientos

