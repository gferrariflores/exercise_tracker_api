from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)
#CORS(app, origins="http://localhost:5173")

# Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/exercise_tracker_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://postgres:postgres@localhost/exercise_tracker_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://gferrariflores:tracker_mysql@gferrariflores.mysql.pythonanywhere-services.com/gferrariflores$exercise-tracker-db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/exercise_tracker_db'
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
    favorite = db.Column(db.Boolean, default=False)  # Added favorite column with default value False

    def __init__(self, name, description, favorite):
        self.name = name
        self.description = description
        self.favorite = favorite

# Crear la tabla usando el contexto de la aplicación Flask
with app.app_context():
    db.create_all()

# Exercise Schema
class ExerciseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'favorite')

# Init Schema
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

# Create an Exercise
@app.route('/exercise', methods=['POST'])
def add_exercise():
    name = request.json['name']
    description = request.json['description']
    favorite = request.json['favorite']

    new_exercise = Exercise(name, description, favorite)

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
    favorite = request.json['favorite']

    exercise.name = name
    exercise.description = description
    exercise.favorite = favorite

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