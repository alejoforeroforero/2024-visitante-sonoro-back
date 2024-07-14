from django_filters import rest_framework as filters
from .models import Record

class MusicFilter(filters.FilterSet):
    # category = filters.CharFilter(lookup_expr='iexact')
    # author = filters.CharFilter(lookup_expr='icontains')

    category = filters.CharFilter(field_name='category__title', lookup_expr='iexact')
    author = filters.CharFilter(field_name='author__title',lookup_expr='icontains')
    title = filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Record
        fields = ['category', 'author', 'title']