from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from publications.models import Publication, Review
from publications.serializers import PublicationSerializer, ReviewSerializer
from users.permissions import IsAdmin, IsPublicationReviewOwner


class PublicationCreateAPIView(generics.CreateAPIView):
    """Класс generics модели Publication для создания поста."""

    serializer_class = PublicationSerializer

    def perform_create(self, serializer):
        """Метод добавляет в поле author пользователя, который создает пост."""

        habit = serializer.save()
        habit.author = self.request.user
        habit.save()


class PublicationListAPIView(generics.ListAPIView):
    """Класс generics модели Publication для вывода списка постов."""

    serializer_class = PublicationSerializer
    permission_classes = (AllowAny,)
    queryset = Publication.objects.all()


class PublicationRetrieveAPIView(generics.RetrieveAPIView):
    """Класс generics модели Publication для вывода информации о посте."""

    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()


class PublicationUpdateAPIView(generics.UpdateAPIView):
    """Класс generics модели Publication обновления информации поста."""

    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()
    permission_classes = [IsAdmin | IsPublicationReviewOwner]


class PublicationDestroyAPIView(generics.DestroyAPIView):
    """Класс generics модели Publication для удаления поста."""

    queryset = Publication.objects.all()
    permission_classes = [IsAdmin | IsPublicationReviewOwner]


class ReviewCreateAPIView(generics.CreateAPIView):
    """Класс generics модели Review для создания отзыва."""

    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        """Метод добавляет в поле author пользователя, который добавляет отзыв."""

        review = serializer.save()
        review.author = self.request.user
        review.save()


class ReviewListAPIView(generics.ListAPIView):
    """Класс generics модели Review для вывода списка отзывов."""

    serializer_class = ReviewSerializer

    def get_queryset(self):
        """Функция для получения списка отзывов. Если админ - то все, пользователь - только свои."""

        return Review.objects.filter(ad=self.kwargs.get("pk"))


class ReviewRetrieveAPIView(generics.RetrieveAPIView):
    """Класс generics модели Review для вывода информации об отзыве."""

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ReviewUpdateAPIView(generics.UpdateAPIView):
    """Класс generics модели Review для обновления информации об отзыве."""

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAdmin | IsPublicationReviewOwner]


class ReviewDestroyAPIView(generics.DestroyAPIView):
    """Класс generics модели Review для удаления отзыва."""

    queryset = Review.objects.all()
    permission_classes = [IsAdmin | IsPublicationReviewOwner]
