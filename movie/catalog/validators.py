from django.core.exceptions import ValidationError


def validate_space_len_comment(text):
    if len(text) == text.count(" "):
        raise ValidationError("Пустой комментарий")
    return True


def validate_length_comment(text):
    if len(text) == 0:
        raise ValidationError("Пустой комментарий")
    return True
