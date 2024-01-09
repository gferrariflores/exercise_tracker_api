from app import ma

class ExerciseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'favorite')

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
