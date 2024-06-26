from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(10), nullable=False)
    lastname = db.Column(db.String(15), nullable=False)
    username = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    
    def __str__(self) -> str:
        return f'Usuario: {self.username}'