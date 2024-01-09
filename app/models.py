from app import db

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    favorite = db.Column(db.Boolean, default=False)

    def __init__(self, name, description, favorite):
        self.name = name
        self.description = description
        self.favorite = favorite
