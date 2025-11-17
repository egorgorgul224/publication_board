from rest_framework.serializers import ValidationError


class TitleValidator:
    """Класс-валидатор для заголовка поста. Если автор вписал в заголовок запрещенные слова, то возбуждается ошибка."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        ban_words = ["ерунда", "глупость", "чепуха"]
        title = dict(value).get(self.field)
        if not title:
            return
        for word in ban_words:
            if word in title.lower():
                raise ValidationError(f"Заголовок содержит запрещенное слово {word}")
