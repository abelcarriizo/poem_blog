from .. import db

likes = db.Table('likes',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('poem_id', db.Integer, db.ForeignKey('poem.id'), primary_key=True)
)
