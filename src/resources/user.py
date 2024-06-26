from .. import db
from src.models import userModel
from flask import jsonify
from flask_restful import Resource

class User(Resource):
    def get(self, id):
        user = db.session.query(userModel).get_or_404(id)
        return user.to_json()

class Users(Resource):
    def get(self):
        users = db.session.query(userModel).all()
        return jsonify([user.to_json() for user in users])
        