from flask import request, jsonify
from app import app, db
from app.models import Exercise
from app.schemas import exercise_schema, exercises_schema

@app.route('/exercise', methods=['POST'])
def add_exercise():
    name = request.json['name']
    description = request.json['description']
    favorite = request.json['favorite']

    new_exercise = Exercise(name, description, favorite)

    db.session.add(new_exercise)
    db.session.commit()

    result = exercise_schema.dump(new_exercise)
    return jsonify({
        'message': 'Exercise added successfully',
        'data': result
    })

@app.route('/exercise', methods=['GET'])
def get_exercises():
    all_exercises = Exercise.query.all()
    result = exercises_schema.dump(all_exercises)
    return jsonify(result)

@app.route('/exercise/<id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get(id)
    return exercise_schema.jsonify(exercise)

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

    result = exercise_schema.dump(exercise)
    return jsonify({
        'message': 'Exercise updated successfully',
        'data': result
    })

@app.route('/exercise/<id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    db.session.delete(exercise)
    db.session.commit()

    result = exercise_schema.dump(exercise)
    return jsonify({
        'message': 'Exercise deleted successfully',
        'data': result
    })
