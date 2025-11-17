from datetime import date

from rest_framework import serializers

from publications.models import Publication, Review
from publications.validators import TitleValidator


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализация модели Review. Предоставлен доступ ко всем полям, кроме author, created_at, updated_at."""

    class Meta:
        model = Review
        exclude = ["author", "created_at", "updated_at"]


class PublicationSerializer(serializers.ModelSerializer):
    """Сериализация модели Publication. Предоставлен доступ ко всем полям, кроме author."""

    validators = [TitleValidator(field="title")]
    review_count = serializers.SerializerMethodField()
    publ_reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = ["id", "review_count", "title", "text", "image", "publ_reviews", "updated_at"]

    def validate(self, value):
        """Метод для валидации возраста пользователя при создании поста. Если автор поста не достиг 18 лет возбуждается
        ошибка."""

        user = self.context["request"].user
        if not user.birthdate:
            raise serializers.ValidationError("Укажите дату рождения в профиле.")

        today = date.today()
        age = (
            today.year - user.birthdate.year - ((today.month, today.day) < (user.birthdate.month, user.birthdate.day))
        )
        if age < 18:
            raise serializers.ValidationError("Вы не можете публиковать пост, так как вы не достигли возраста 18 лет.")
        return value

    def get_review_count(self, obj):
        """Метод для подсчета количества отзывов в объявлении. 'publ_reviews' - related_name поля 'publication'
        модели Review."""

        return obj.publ_reviews.count()
