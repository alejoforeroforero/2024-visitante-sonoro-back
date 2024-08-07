from rest_framework import viewsets


# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import RecordSerializerData, CategorySerializer, AuthorSerializer, TagSerializer, RecordSerializerFront, AuthorSerializerFront
from .models import Record, Category, Author, Tag
from .filters import MusicFilter

User = get_user_model()


# class SignupView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         first_name = request.data.get('first_name', '')
#         last_name = request.data.get('last_name', '')

#         if User.objects.filter(email=email).exists():
#             return Response({'success': False, 'message': 'Email already exists'}, status=status.HTTP_200_OK)

#         user = User.objects.create_user(
#             email=email,
#             password=password,
#             first_name=first_name,
#             last_name=last_name
#         )
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({
#             'success': True,
#             'token': token.key,
#             'user': {
#                 'id': user.id,
#                 'email': user.email,
#                 'first_name': user.first_name,
#                 'last_name': user.last_name,
#             }
#         }, status=status.HTTP_200_OK)


# class SigninView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({
#                 'success': True,
#                 'token': token.key,
#                 'user': {
#                     'id': user.id,
#                     'email': user.email,
#                     'first_name': user.first_name,
#                     'last_name': user.last_name,
#                 }
#             }, status=status.HTTP_200_OK)
#         return Response({
#             'success': False,
#             'message': 'Invalid credentials'
#         }, status=status.HTTP_200_OK)

# class SignoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         request.auth.delete()
#         return Response({'success': True, 'message': ''}, status=status.HTTP_200_OK)

# class UserDataView(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer


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
