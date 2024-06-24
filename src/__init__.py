from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import src.resources as resources

api = Api() #Inicializa API de Flask Restful

# Método que inicializará todos los módulos y devolverá la aplicación
def create_app():
    app = Flask(__name__) #Inicializa Flask

    load_dotenv() #Carga las variables de entorno
    
    #Carga a la API los recursos
    #Todos los recursos
    api.add_resource(resources.UsersResource, '/users')
    #Recursos por ID
    api.add_resource(resources.UserResource, '/user/<id>')

    api.init_app(app) #Cargar la aplicacion en la API de Flask Restful

    return app