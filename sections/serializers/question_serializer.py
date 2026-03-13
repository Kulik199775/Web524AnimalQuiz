from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField

from sections.models import Section, Question


class QuestionSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'section', 'question')


class QuestionSectionSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())
    question = CharField()
    member_answer = CharField(write_only=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'section', 'question', 'member_answer')