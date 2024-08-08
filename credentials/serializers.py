
from rest_framework import serializers
from recordings.serializer import RecordSerializerData2
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['email'],
        )
        return user


class ExtendedUserSerializer(serializers.ModelSerializer):

    favorite_records = RecordSerializerData2(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name',
                  'last_name', 'bio', 'birth_date', 'phone_number',
                  'address', 'is_active', 'profile_picture',
                  'google_picture', 'google_id', 'date_joined', 'favorite_records'
                  ]
        read_only_fields = ('id', 'email', 'google_picture',
                            'google_id', 'date_joined', 'favorite_records')


class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_picture']
