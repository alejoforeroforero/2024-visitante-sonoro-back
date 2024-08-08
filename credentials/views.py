from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import (
    UserSerializer,
    ExtendedUserSerializer,
    ProfilePictureSerializer
)
from google.oauth2 import id_token
from google.auth.transport import requests
from recordings.models import Record

User = get_user_model()


class RegisterView(APIView):

    def post(self, request):

        email = request.data.get('email')

        if User.objects.filter(email=email).exists():
            return Response({'success': False, 'message': 'Email already exists'}, status=status.HTTP_200_OK)

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response = Response({
                'success': True,
                'message': 'Check your email for verification',
                'access': str(refresh.access_token),
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
            response.set_cookie(
                'refresh_token',
                str(refresh),
                httponly=True,
                samesite='Strict',
                secure=True,
                max_age=24 * 60 * 60
            )
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleSignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.data.get('token')

        try:
            # Verify the Google token
            idinfo = id_token.verify_oauth2_token(
                token, requests.Request(), settings.GOOGLE_CLIENT_ID)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')

            user_data = {'username': idinfo['email'],
                         'email': idinfo['email'],
                         'first_name': idinfo.get('given_name'),
                         'password': '',
                         'google_id': idinfo['sub'],
                         'google_picture': idinfo.get('picture'),
                         }

            if User.objects.filter(email=user_data['email']).exists():
                user = User.objects.get(email=user_data['email'])

                serializer = ExtendedUserSerializer(
                    user, data=user_data, partial=True)

                if serializer.is_valid():
                    # user = serializer.save()
                    refresh = RefreshToken.for_user(user)
                    response = Response({
                        'success': True,
                        'message': 'Loggin succesfull',
                        'access': str(refresh.access_token),
                        'user': serializer.data
                    }, status=status.HTTP_200_OK)
                    response.set_cookie(
                        'refresh_token',
                        str(refresh),
                        httponly=True,
                        samesite='Strict',
                        secure=True,
                        max_age=24 * 60 * 60
                    )
                    access_token = response.data['access']
                    response.set_cookie(
                        'access_token',
                        access_token,
                        samesite='Strict',
                        secure=True,
                        max_age=5 * 60
                    )

                return response
            else:
                user = User.objects.create_user(
                    email=user_data['email'],
                    username=user_data['email'],
                    google_id=user_data['google_id'],
                    google_picture=user_data['google_picture'],
                    password=user_data.get('password', '')
                )

                serializer = ExtendedUserSerializer(
                    user, data=user_data, partial=True)

                if serializer.is_valid():
                    user = serializer.save()
                    refresh = RefreshToken.for_user(user)
                    response = Response({
                        'success': True,
                        'message': 'Loggin succesfull',
                        'access': str(refresh.access_token),
                        'user': serializer.data
                    }, status=status.HTTP_200_OK)
                    response.set_cookie(
                        'refresh_token',
                        str(refresh),
                        httponly=True,
                        samesite='Strict',
                        secure=True,
                        max_age=24 * 60 * 60
                    )
                    access_token = response.data['access']
                    response.set_cookie(
                        'access_token',
                        access_token,
                        samesite='Strict',
                        secure=True,
                        max_age=5 * 60
                    )
                return response

        except ValueError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = ExtendedUserSerializer(user)
        data = serializer.data
        data['profile_picture'] = request.build_absolute_uri(
            user.profile_picture.url) if user.profile_picture else None

        return Response({'success': True, 'data': data}, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = ExtendedUserSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data['profile_picture'] = request.build_absolute_uri(
                user.profile_picture.url) if user.profile_picture else None

            return Response({'success': True, 'data': data, }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateFavoriteRecordsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        record_id = request.data.get('record_id')

        if not record_id:
            return Response({'success': False, 'message': 'No record id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            record = Record.objects.get(id=record_id)
        except Record.DoesNotExist:
            return Response({'success': False, 'message': 'No record found'}, status=status.HTTP_404_NOT_FOUND)

        user.favorite_records.add(record)

        serializer = ExtendedUserSerializer(user)
        return Response(serializer.data)
    
    def delete(self, request):
        user = request.user
        record_id = request.data.get('record_id')

        if not record_id:
            return Response({'success': False, 'message': 'No record found'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            record = Record.objects.get(id=record_id)
        except Record.DoesNotExist:
            return Response({'success': False, 'message': 'No record found'}, status=status.HTTP_404_NOT_FOUND)

        user.favorite_records.remove(record)

        serializer = ExtendedUserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            response = Response(
                {"message": "Successfully logged out."}, status=status.HTTP_200_OK)
            response.delete_cookie('refresh_token')
            response.delete_cookie('access_token')
            return response
        except TokenError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        if not User.objects.filter(email=email).exists():
            return Response(
                {'success': False, 'message': 'The credentials you entered are incorrect. Please try again.'},
                status=status.HTTP_200_OK
            )

        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            data = response.data if hasattr(response, 'data') else {}
            data['message'] = "Login successful! You are now logged in"
            data['success'] = True

            refresh_token = response.data['refresh']
            response.set_cookie(
                'refresh_token',
                refresh_token,
                httponly=True,
                samesite='Strict',
                secure=True,
                max_age=24 * 60 * 60
            )
            del response.data['refresh']

            access_token = response.data['access']
            response.set_cookie(
                'access_token',
                access_token,
                samesite='Strict',
                secure=True,
                max_age=5 * 60
            )
        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh_token')
        if refresh_token:
            request.data['refresh'] = refresh_token
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            new_refresh_token = response.data.get('refresh')
            if new_refresh_token:
                response.set_cookie(
                    'refresh_token',
                    new_refresh_token,
                    httponly=True,
                    samesite='Strict',
                    secure=True,  # set to True if using HTTPS
                    max_age=24 * 60 * 60  # 1 day in seconds
                )
                # Remove new refresh token from response body
                del response.data['refresh']
        return response


class UpdateProfilePictureView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProfilePictureSerializer(
            request.user, data=request.data, partial=True)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({
                'success': True,
                'message': 'Profile picture updated successfully',
                'profile_picture': request.build_absolute_uri(instance.profile_picture.url) if instance.profile_picture else None,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
