import re

from rest_framework.serializers import ValidationError


class PasswordValidator:
    """Класс-валидатор для проверки пароля. Если пароль меньше 8 символов и/или не содержит цифры, то возбуждается
    ошибка."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        password = dict(value).get(self.field)
        if len(password) < 8:
            raise ValidationError("Пароль должен быть не менее 8 символов.")
        is_digit = any(number.isdigit() for number in password)
        if not is_digit:
            raise ValidationError("Пароль должен содержать цифры.")


class MailValidator:
    """Класс-валидатор для проверки почты. Если домен указанной почты не разрешен, возбуждается ошибка(разрешены
    домены: mail.ru, yandex.ru)."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        mail = dict(value).get(self.field)
        mail_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@mail.ru$")
        yandex_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@yandex.ru$")
        is_valid = 0
        for pattern in [mail_pattern, yandex_pattern]:
            if re.match(pattern, mail):
                is_valid += 1
        if not is_valid:
            raise ValidationError("Неверно указана почта. Разрешены домены: mail.ru, yandex.ru")
