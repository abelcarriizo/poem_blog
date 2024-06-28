from .. import db

class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    description = db.Column(db.String(255)) #Descripcion breve del poema
    content = db.Column(db.Text, nullable=False) #Contenido extenso del poema

    def __repr__(self):
        return f'Titulo: {self.title}, Género: {self.genre}, Fecha: {self.date_created}, Descripción: {self.description}'
    
    #Convertir objeto a JSON
    def to_json(self):
        poem_json = {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            'date_created': self.date_created.isoformat(),
            "description": self.description,
            "content": self.content
        }
        return poem_json

    #Convertir JSON a objeto
    def from_json(poem_json):
        id = poem_json.get("id")
        title = poem_json.get("title")
        author = poem_json.get("author")
        genre = poem_json.get("genre")
        date_created = poem_json.get("date_created")
        description = poem_json.get("description")
        content = poem_json.get("content")
        return Poem(id=id, title=title, author=author, genre=genre, date_created=date_created, description=description, content=content)
