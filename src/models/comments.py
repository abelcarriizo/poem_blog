from .. import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    content = db.Column(db.String(255))

    def __repr__(self) -> str:
        return f'Autor: {self.author}, Contenido: {self.content}'
    
    def to_json(self):
        comment_json = {
            "id": self.id,
            "author": self.author,
            "date_created": self.date_created.isoformat(),
            "content": self.content
        }
        return comment_json

    def from_json(comment_json):
        id = comment_json.get("id")
        author = comment_json.get("author")
        date_created = comment_json.get("date_created")
        content = comment_json.get("content")
        return Comment(id=id, author=author, date_created=date_created, content=content)