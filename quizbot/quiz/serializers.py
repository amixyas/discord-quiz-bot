from rest_framework.serializers import ModelSerializer
from .models import Question, Answer
from .models import Answer


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class RandomQuestionSerializer(ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            'title', 'answer'
        ]
        