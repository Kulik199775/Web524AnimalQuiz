from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, Content, Question
from sections.permissions import IsModerator, IsSuperUser
from sections.serializers.section_serializers import SectionSerializer, SectionListSerializer
from sections.serializers.content_serializers import ContentSerializer, ContentListSerializer
from sections.serializers.question_serializer import QuestionSerializer, QuestionSectionSerializer
from sections.paginators import SectionPaginator, ContentPaginator, QuestionPaginator


class SectionListAPIView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)


class ContentListAPIView(ListAPIView):
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = ContentPaginator


class ContentCreateAPIView(CreateAPIView):
    serializer_class = ContentSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class ContentRetrieveAPIView(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)


class ContentUpdateAPIView(UpdateAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class ContentDestroyAPIView(DestroyAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = QuestionPaginator


class QuestionRetrieveAPIView(RetrieveAPIView):
    serializer_class = QuestionSectionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        question = self.get_object()

        if not question.answer:
            return Response(
                {'error': 'У этого вопроса нет правильного ответа'},
                status=400
            )

        member_answer = request.data.get('member_answer')
        if not member_answer:
            return Response(
                {'error': 'Не указан ответ'},
                status=400
            )

        correct = question.answer.title.strip().lower()
        user = member_answer.strip().lower()
        is_correct = (user == correct)

        response_data = {
            'is_correct': is_correct,
            'your_answer': member_answer,
            'question_id': question.id,
            'question': question.question,
            'correct_answer': question.answer.title if not is_correct else None,
            'explanation': question.description
        }

        return Response(response_data)