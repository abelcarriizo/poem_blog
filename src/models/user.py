from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(10), nullable=False)
    lastname = db.Column(db.String(15), nullable=False)
    username = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    
    def __repr__(self) -> str:
        return f'Usuario: {self.username}'
    
    #Convertir objeto a JSON
    def to_json(self):
        user_json = {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "description": self.description,
            "email": self.email,
            "password": self.password
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