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
    def get(self, poem_id):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        comments_pagination = db.session.query(CommentModel).filter_by(poem_id=poem_id).order_by(CommentModel.date_created).paginate(page=page, per_page=per_page, error_out=False)
        
        data = {
            'total': comments_pagination.total,
            'pages': comments_pagination.pages,
            'current_page': comments_pagination.page,
            'next_page': comments_pagination.next_num,
            'prev_page': comments_pagination.prev_num,
            'has_next': comments_pagination.has_next,
            'has_prev': comments_pagination.has_prev,
            'items': [comment.to_json() for comment in comments_pagination.items]
        }
        
        return jsonify(data)
    
    def post(self):
        comment = CommentModel.from_json(request.get_json())
        db.session.add(comment)
        db.session.commit()
        return comment.to_json(), 201