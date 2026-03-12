from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, Content
from sections.permissions import IsModerator, IsSuperUser
from sections.serializers.section_serializers import SectionSerializer, SectionListSerializer
from sections.serializers.content_serializers import (ContentSerializer, ContentListSerializer)
from sections.paginators import SectionPaginator, ContentPaginator


class SectionListAPIView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated,)
    pagination_class = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated,)


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated, IsSuperUser)


class ContentListAPIView(ListAPIView):
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated,)
    pagination_class = ContentPaginator


class ContentCreateAPIView(CreateAPIView):
    serializer_class = ContentSerializer
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class ContentRetrieveAPIView(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated,)


class ContentUpdateAPIView(UpdateAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class ContentDestroyAPIView(DestroyAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated, IsSuperUser)
