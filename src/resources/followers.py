from .. import db
from src.models import UserModel
from flask import jsonify
from flask_restful import Resource

class Follow(Resource):
    def post(self, user_id, follower_id):
        if user_id == follower_id:
            return {"message": "Un usuario no puede seguirse a sí mismo"}, 404
        
        user = db.session.query(UserModel).get_or_404(user_id)
        follower = db.session.query(UserModel).get_or_404(follower_id)

        if follower not in user.followers:
            user.followers.append(follower)
            db.session.commit()
            return {"message": f"{follower.username} ahora sigue a {user.username}"}, 201
        return {"message": f"{follower.username} ya sigue a {user.username}"}, 200
    
    def delete(self, user_id, follower_id):
        if user_id == follower_id:
            return {"message": "Un usuario no puede dejar de seguirse a sí mismo"}, 404
        
        user = db.session.query(UserModel).get_or_404(user_id)
        follower = db.session.query(UserModel).get_or_404(follower_id)

        if follower in user.followers:
            user.followers.remove(follower)
            db.session.commit()
            return {"message": f"{follower.username} ha dejado de seguir a {user.username}"}, 200
        return {"message": f"{follower.username} no sigue a {user.username}"}, 400

class Follower(Resource):
    def get(self, user_id):
        user = db.session.query(UserModel).get_or_404(user_id)
        followers = user.followers.all()  # Assuming you have a 'followers' relationship in User model
        return jsonify([follower.to_json() for follower in followers])

class Followed(Resource):
    def get(self, user_id):
        user = db.session.query(UserModel).get_or_404(user_id)
        followed_users = user.followed.all()  # Assuming you have a 'followed' relationship in User model
        return jsonify([followed.to_json() for followed in followed_users])
