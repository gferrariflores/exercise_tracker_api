from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/exercise_tracker_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Exercise Class/Model
class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Exercise Schema
class ExerciseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')

# Init Schema
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

# Create an Exercise
@app.route('/exercise', methods=['POST'])
def add_exercise():
    name = request.json['name']
    description = request.json['description']

    new_exercise = Exercise(name, description)

    db.session.add(new_exercise)
    db.session.commit()

    return exercise_schema.jsonify(new_exercise)

# Get All Exercises
@app.route('/exercise', methods=['GET'])
def get_exercises():
    all_exercises = Exercise.query.all()
    result = exercises_schema.dump(all_exercises)
    return jsonify(result)

# Get Single Exercise
@app.route('/exercise/<id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get(id)
    return exercise_schema.jsonify(exercise)

# Update an Exercise
@app.route('/exercise/<id>', methods=['PUT'])
def update_exercise(id):
    exercise = Exercise.query.get(id)
    name = request.json['name']
    description = request.json['description']

    exercise.name = name
    exercise.description = description

    db.session.commit()

    return exercise_schema.jsonify(exercise)

# Delete Exercise
@app.route('/exercise/<id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    db.session.delete(exercise)
    db.session.commit()

    return exercise_schema.jsonify(exercise)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)