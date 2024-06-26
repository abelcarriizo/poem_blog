from .. import db
from flask import request, jsonify
from flask_restful import Resource
from src.models import PoemModel

class Poem(Resource):
    def get(self, id):
        poem = db.session.query(PoemModel).get_or_404(id)
        return poem.to_json()
    
    def put(self, id):
        poem = db.session.query(PoemModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(poem, key, value)
        db.session.add(poem)
        db.session.commit()
        return poem.to_json(), 201
    
    def delete(self,id):
        poem = db.session.query(PoemModel).get_or_404(id)
        db.session.delete(poem)
        db.session.commit()
        return '', 204

class Poems(Resource):
    def get(self):
        poems = db.session.query(PoemModel).all()
        print(poems)
        return jsonify([poem.to_json() for poem in poems])

    def post(self):
        poem = PoemModel.from_json(request.get_json())
        db.session.add(poem)
        db.session.commit()
        return poem.to_json(), 201