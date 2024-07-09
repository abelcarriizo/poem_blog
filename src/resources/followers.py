from .. import db
from src.models import UserModel
from flask import jsonify, request
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
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        user = db.session.query(UserModel).get_or_404(user_id)
        followers_pagination = user.followers.paginate(page=page, per_page=per_page, error_out=False)
        
        data = {
            'total': followers_pagination.total,
            'pages': followers_pagination.pages,
            'current_page': followers_pagination.page,
            'next_page': followers_pagination.next_num,
            'prev_page': followers_pagination.prev_num,
            'has_next': followers_pagination.has_next,
            'has_prev': followers_pagination.has_prev,
            'items': [follower.to_json() for follower in followers_pagination.items]
        }
        
        return jsonify(data)

class Followed(Resource):
    def get(self, user_id):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        user = db.session.query(UserModel).get_or_404(user_id)
        followed_pagination = user.followed.paginate(page=page, per_page=per_page, error_out=False)
        
        data = {
            'total': followed_pagination.total,
            'pages': followed_pagination.pages,
            'current_page': followed_pagination.page,
            'next_page': followed_pagination.next_num,
            'prev_page': followed_pagination.prev_num,
            'has_next': followed_pagination.has_next,
            'has_prev': followed_pagination.has_prev,
            'items': [followed.to_json() for followed in followed_pagination.items]
        }
        
        return jsonify(data)
