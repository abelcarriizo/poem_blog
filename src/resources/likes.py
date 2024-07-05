from .. import db
from flask import jsonify
from flask_restful import Resource
from src.models import UserModel, PoemModel

class Like(Resource):
    def post(self, poem_id, user_id):
        poem = db.session.query(PoemModel).get_or_404(poem_id)
        user = db.session.query(UserModel).get_or_404(user_id)

        if user in poem.liked_by:
            return {"message": "El usuario ya ha dado like a este poema"}, 200
        
        poem.liked_by.append(user)
        db.session.commit()
        return {"message": f"El usuario {user.username} ha dado like al poema {poem.title}"}, 201

    def delete(self, poem_id, user_id):
        poem = db.session.query(PoemModel).get_or_404(poem_id)
        user = db.session.query(UserModel).get_or_404(user_id)

        if user not in poem.liked_by:
            return {"message": "El usuario no ha dado like a este poema"}, 400
        
        poem.liked_by.remove(user)
        db.session.commit()
        return {"message": f"El usuario {user.username} ha quitado su like al poema {poem.title}"}, 200

class Likes(Resource):
    def get(self, poem_id):
        poem = db.session.query(PoemModel).get_or_404(poem_id)
        like_count = poem.liked_by.count()
        return jsonify({"like_count": like_count})