from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import RecordSerializerData, CategorySerializer, AuthorSerializer, TagSerializer, RecordSerializerFront, AuthorSerializerFront
from .models import Record, Category, Author, Tag
from .filters import MusicFilter

class RecordingsDataView(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('id')
    serializer_class = RecordSerializerData


class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AuthorsView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorsViewFront(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializerFront

class TagView(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class RecordingsView(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('id')
    serializer_class = RecordSerializerFront

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializerFront
    filter_backends = [DjangoFilterBackend]
    filterset_class = MusicFilter
