import os
import json
import sys
sys.path.append('src/ci-345_controles-valores-de-unidad-de-fondo')

import datetime as dt
import numpy as np
import pandas as pd

from marshmallow import Schema, fields
from flask import Flask, Request, abort, request
from dotenv import load_dotenv

from API.modelo import IF

BAD_REQUEST = "400"

load_dotenv()
src_path = os.path.dirname(os.path.dirname(__file__))

HOST = os.getenv("HOST")
PORT = os.getenv("PORT", 8080)

alerta = IF()

class MatrizDatos(Schema):
    """
    Se validan los datos de entrada
    """
    
    Fecha = fields.String(required = True)
    NEMOTECNICO = fields.String(required = True)
    valor = fields.Float(required = True)
    clase = fields.String(required = True)
    pago = fields.Float(required = True)

def obtener_alerta(request: Request):
    """
    Función que recibe la información del json para un request y
    retorna la clasificación.

    Args:
    ----------
    request_data: Request
        Objeto con la solicitud HTTP realizada al app

    Results:
    ----------
    Alerta que arroja el modelo 
    """


    request_data = request.get_json()

    val_request = MatrizDatos()

    errors = val_request.validate(request_data)
    if errors: 
        abort(int(BAD_REQUEST), str(errors))
    
    lanzar_alerta = alerta.generar_alerta(request_data['Fecha'],request_data['NEMOTECNICO'],request_data['valor'],request_data['clase'],request_data['pago'])

    return lanzar_alerta


def create_app(test_config=None):
    """
    Función para la creación y configuración del app
    """

    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/home')
    def home_fun():
        return "Hello world"

    @app.route('/IsolationForest/home', methods = ['POST'])
    def generar_alerta():
        alerta = obtener_alerta(request)
        json_res = {"alerta": alerta}
        response = json.dumps(json_res).encode("utf-8")
        return response, 200, {"Accept": "application/json"}

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=PORT)
