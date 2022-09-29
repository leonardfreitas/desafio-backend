from rest_framework import serializers

from .models import Option, Question, Quiz
from apps.categories.serializers import CategorySerializer


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = ['id', 'name', 'is_correct', 'created_at', 'updated_at']


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'name', 'created_at', 'updated_at']


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'category', 'questions', 'created_at', 'updated_at']


class DetailQuestionSerializer(serializers.ModelSerializer):
    option_set = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'name', 'created_at', 'updated_at', 'option_set']


class DetailQuizSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    questions = DetailQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'category', 'questions', 'created_at', 'updated_at']
