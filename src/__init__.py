import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

api = Api() #Inicializa API de Flask Restful
db = SQLAlchemy() #Inicializa SQLAlchemy

# Método que inicializará todos los módulos y devolverá la aplicación
def create_app():
    app = Flask(__name__) #Inicializa Flask

    load_dotenv() #Carga las variables de entorno

    #Si no existe el archivo de base de datos crearlo (solo válido si se utiliza SQLite)
    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    #Configuracion de Base de Datos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@localhost/{os.getenv('DATABASE_NAME')}'

    db.init_app(app)

    import src.resources as resources
    
    #Carga a la API los recursos
    #Todos los recursos
    api.add_resource(resources.UsersResource, '/users')
    api.add_resource(resources.PoemsResource, '/poems')
    #Recursos por ID
    api.add_resource(resources.UserResource, '/user/<id>')
    api.add_resource(resources.PoemResource, '/poem/<id>')

    api.init_app(app) #Cargar la aplicacion en la API de Flask Restful

    return app