from .. import db
from src.models import userModel
from flask import jsonify, request
from flask_restful import Resource

class User(Resource):
    def get(self, id):
        user = db.session.query(userModel).get_or_404(id)
        print(user)
        return user.to_json()

class Users(Resource):
    def get(self):
        users = db.session.query(userModel).all()
        return jsonify([user.to_json() for user in users])
        
    def post(self):
        user = userModel.from_json(request.get_json())
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201