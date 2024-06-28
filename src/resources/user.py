from .. import db
from src.models import userModel
from flask import jsonify, request
from flask_restful import Resource

class User(Resource):
    def get(self, id):
        user = db.session.query(userModel).get_or_404(id)
        print(user)
        return user.to_json()
    
    def put(self, id):
        user = db.session.query(userModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(user, key, value)
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201
    
    def delete(self, id):
        user = db.session.query(userModel).get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

class Users(Resource):
    def get(self):
        users = db.session.query(userModel).all()
        return jsonify([user.to_json() for user in users])
        
    def post(self):
        user = userModel.from_json(request.get_json())
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201