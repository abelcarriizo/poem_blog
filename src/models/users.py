from .. import db
from .followers import followers
from .likes import likes

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(10), nullable=False)
    lastname = db.Column(db.String(15), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    poems = db.relationship('Poem', back_populates='author', cascade='all, delete-orphan')
    comments = db.relationship('Comment', back_populates='author', cascade='all, delete-orphan')
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic'
    )
    liked_poems = db.relationship('Poem', secondary=likes, back_populates='liked_by')

    #Convertir objeto a JSON
    def to_json(self):
        user_json = {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "description": self.description,
            "email": self.email,
        }
        return user_json

    #Convertir JSON a objeto
    @staticmethod
    def from_json(user_json):
        id = user_json.get("id")
        firstname = user_json.get("firstname")
        lastname = user_json.get("lastname")
        username = user_json.get("username")
        description = user_json.get("description")
        email = user_json.get("email")
        password = user_json.get("password")
        return User(id=id, firstname=firstname, lastname=lastname, username=username, description=description, email=email, password=password)
