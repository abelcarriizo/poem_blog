from .. import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    poem_id = db.Column(db.Integer, db.ForeignKey('poem.id'), nullable=False)
    date_created = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    content = db.Column(db.String(255))

    author = db.relationship('User', back_populates='comments')
    poem = db.relationship('Poem', back_populates='comments')
    
    #Convertir objeto a JSON
    def to_json(self):
        comment_json = {
            "id": self.id,
            "author_id": self.author_id,
            "poem_id": self.poem_id,
            "date_created": self.date_created.isoformat(),
            "content": self.content
        }
        return comment_json

    #Convertir JSON a objeto
    @staticmethod
    def from_json(comment_json):
        id = comment_json.get("id")
        author_id = comment_json.get("author_id")
        poem_id = comment_json.get("poem_id")
        date_created = comment_json.get("date_created")
        content = comment_json.get("content")
        return Comment(id=id, author_id=author_id, poem_id=poem_id, date_created=date_created, content=content)