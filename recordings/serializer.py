from rest_framework import serializers
from .models import Record, Category, Author, Tag


class RecordSerializerData(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'


class RecordSerializerData2(serializers.ModelSerializer):

    category = serializers.CharField(
        source='category.title', read_only=True)
    
    author = serializers.CharField(
        source='author.title', read_only=True)

    class Meta:
        model = Record
        fields = ['id', 'title', 'audio', 'author', 'category', 'tags']


class CategorySerializer(serializers.ModelSerializer):
    recordings = RecordSerializerData(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'recordings']


class AuthorSerializer(serializers.ModelSerializer):
    recordings = RecordSerializerData(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'title', 'description', 'image', 'recordings']


class AuthorSerializerFront(serializers.ModelSerializer):
    recordings = RecordSerializerData2(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'title', 'description', 'image', 'recordings']


class TagSerializer(serializers.ModelSerializer):
    recordings = RecordSerializerData(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'title', 'recordings']


class TagSerializerFront(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'title']


class RecordSerializerFront(serializers.ModelSerializer):
    category = serializers.CharField(
        source='category.title', read_only=True)

    author = serializers.CharField(
        source='author.title', read_only=True)

    tags = TagSerializerFront(many=True, read_only=True)

    class Meta:
        model = Record
        fields = ['id', 'title', 'image', 'description',
                  'audio', 'latitude', 'longitude', 'category', 'author', 'tags']
