from .. import db
from src.models import CommentModel
from flask import jsonify, request
from flask_restful import Resource

class Comment(Resource):
    def get(self, id):
        comment = db.session.query(CommentModel).get_or_404(id)
        return comment.to_json()
    
    def put(self, id):
        comment = db.session.query(CommentModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(comment, key, value)
        db.session.add(comment)
        db.session.commit()
        return comment.to_json(), 201
    
    def delete(self, id):
        comment = db.session.query(CommentModel).get_or_404(id)
        db.session.delete(comment)
        db.session.commit()
        return '', 204
    
class Comments(Resource):
    def get(self):
        comments = db.session.query(CommentModel).all()
        return jsonify([comment.to_json() for comment in comments])
    
    def post(self):
        comment = CommentModel.from_json(request.get_json())
        db.session.add(comment)
        db.session.commit()
        return comment.to_json(), 201