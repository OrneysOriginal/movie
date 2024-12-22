from django.db import models
from django.contrib.auth.models import User

from core.models import AbstractImageModel


class Profile(AbstractImageModel):
    birthday = models.DateField()
    image = models.ImageField(upload_to="photo/%y/%m/%d")
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        related_query_name="user",
    )
