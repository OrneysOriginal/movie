from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class AbstractImageModel(models.Model):
    def get_image200x200(self):
        return get_thumbnail(self.image, "200x200", crop="center", quality=51)

    def image_tmb(self):
        if self.image:
            tag = f'<img src="{self.get_image200x200().url}">'
            return mark_safe(tag)

        return mark_safe("<p>изображение отсутствует</p>")

    class Meta:
        abstract = True
