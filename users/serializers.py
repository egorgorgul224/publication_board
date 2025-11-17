from rest_framework import serializers

from users.models import User
from users.validators import MailValidator, PasswordValidator


class UserSerializer(serializers.ModelSerializer):
    """Сериализация модели User. Предоставлен доступ к полям: email, first_name, last_name, birthdate, phone,
    date_joined."""

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "birthdate", "phone", "date_joined"]


class UserMinInfoSerializer(serializers.ModelSerializer):
    """Дополнительная сериализация модели User для обычных пользователей. Предоставлен доступ к полям: last_name,
    first_name, date_joined."""

    class Meta:
        model = User
        fields = ["last_name", "first_name", "date_joined"]


class RegisterUserSerializer(serializers.ModelSerializer):
    """Сериализация модели User для регистрации/создания пользователя. Предоставлен доступ к полям: email."""

    validators = [PasswordValidator(field="password"), MailValidator(field="email")]

    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
