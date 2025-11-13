from django.urls import path

from publications.apps import PublicationsConfig
from publications.views import (PublicationCreateAPIView, PublicationDestroyAPIView, PublicationListAPIView,
                                PublicationRetrieveAPIView, PublicationUpdateAPIView,
                                ReviewCreateAPIView, ReviewDestroyAPIView, ReviewListAPIView, ReviewRetrieveAPIView,
                                ReviewUpdateAPIView)

app_name = PublicationsConfig.name

urlpatterns = [
    # ссылки для модели Ad объявление
    path("publications/create/", PublicationCreateAPIView.as_view(), name="publication_create"),
    path("publications/", PublicationListAPIView.as_view(), name="publication_list"),
    path("publications/<int:pk>/detail/", PublicationRetrieveAPIView.as_view(), name="publication_detail"),
    path("publications/<int:pk>/update/", PublicationUpdateAPIView.as_view(), name="publication_update"),
    path("publications/<int:pk>/delete/", PublicationDestroyAPIView.as_view(), name="publication_delete"),
    # ссылки для модели Review отзыв
    path("review/create/", ReviewCreateAPIView.as_view(), name="review_create"),
    path("review/publication/<int:pk>/", ReviewListAPIView.as_view(), name="review_list"),
    path("review/<int:pk>/detail/", ReviewRetrieveAPIView.as_view(), name="review_detail"),
    path("review/<int:pk>/update/", ReviewUpdateAPIView.as_view(), name="review_update"),
    path("review/<int:pk>/delete/", ReviewDestroyAPIView.as_view(), name="review_delete"),
]
