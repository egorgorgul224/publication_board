from django.db import models

from config import settings


class Publication(models.Model):
    """Модель поста. Содержит поля title, text, image, author, created_at, updated_at."""

    title = models.CharField(max_length=100, verbose_name="Заголовок поста")
    text = models.TextField(verbose_name="Текст поста")
    image = models.ImageField(upload_to="post/", verbose_name="Изображение поста", blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="publications", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}: {self.author} - {self.created_at}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["created_at"]


class Review(models.Model):
    """Модель отзыв. Содержит поля text, author, publication, created_at, updated_at."""

    text = models.TextField(verbose_name="Текст отзыва")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="author_reviews", blank=True, null=True
    )
    publication = models.ForeignKey(
        Publication, on_delete=models.CASCADE, related_name="publ_reviews", verbose_name="Пост"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.publication}: {self.author} - {self.created_at}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["created_at"]
