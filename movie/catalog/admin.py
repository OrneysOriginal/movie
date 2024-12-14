from django.contrib import admin
from catalog.models import Film, Genre, Comment


@admin.register(Film)
class AdminCatalog(admin.ModelAdmin):
    list_display = (
        Film.name.field.name,
        Film.genre.field.name,
        Film.mark.field.name,
        Film.is_eighteen.field.name,
        Film.description.field.name,
    )


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = (Genre.name.field.name,)


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = (Comment.comment.field.name,)
