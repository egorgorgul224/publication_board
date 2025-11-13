from rest_framework import serializers

from publications.models import Publication, Review


class PublicationSerializer(serializers.ModelSerializer):
    """Сериализация модели Publication. Предоставлен доступ ко всем полям, кроме author."""

    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = ["id", "review_count", "title", "image", "created_at", "updated_at"]

    def get_review_count(self, obj):
        """Метод для подсчета количества отзывов в объявлении. 'publ_reviews' - related_name поля 'publication'
        модели Review."""

        return obj.publ_reviews.count()


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализация модели Review. Предоставлен доступ ко всем полям, кроме author, created_at, updated_at."""

    class Meta:
        model = Review
        exclude = ["author", "created_at", "updated_at"]
