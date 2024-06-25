from flask_restful import Resource
from flask import request
from src.database import commentsDB

class Comment(Resource):
    def get(self, id):
        if int(id) in commentsDB:
            return commentsDB[int(id)]
        return '', 404
    
    def put(self, id):
        if int(id) in commentsDB:
            comment = commentsDB[int(id)]
            data = request.get_json()
            comment.update(data)
            return comment, 201
        return '', 404
    
    def delete(self, id):
        if int(id) in commentsDB:
            del commentsDB[int(id)]
            return '', 204
        return '', 404

class Comments(Resource):
    def get(self):
        return commentsDB
    
    def post(self):
        id = int(max(commentsDB.keys())) + 1
        comment = request.get_json()
        commentsDB[id] = comment
        return comment, 201