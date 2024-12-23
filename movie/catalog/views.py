from django.shortcuts import render, redirect, reverse
from django.contrib.messages import error, success
from django.views import View

from catalog.forms import CommentForm
from catalog.models import Film, Genre, Comment
from catalog.validators import (
    validate_space_len_comment,
    validate_length_comment,
)


class CatalogView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            context = {
                "films": Film.objects.all().only(
                    "id", "name", "description", "image"
                ),
            }
            return render(self.request, "catalog/catalog.html", context)

        error(self.request, "Вы не вошли в аккаунт")
        return redirect(reverse("person:login"))

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            pass

        error(self.request, "Вы не вошли в аккаунт")
        return redirect(reverse("person:login"))


class ItemView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            context = {
                "film": Film.objects.get(id=kwargs.get("pk")),
                "genres": Genre.objects.filter(film__id=kwargs.get("pk")),
                "comment_form": CommentForm(),
                "comments": Comment.objects.select_related("film").only(
                    "film", "user", "comment"
                ),
            }
            return render(self.request, "catalog/item.html", context)

        error(self.request, "Вы не вошли в аккаунт")
        return redirect(reverse("person:login"))

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            comment = self.request.POST.get("comment")
            if self.check_length_comment(comment):
                self.add_comment(comment, self.request.user, kwargs.get("pk"))
                success(self.request, "")
                return redirect(
                    reverse("catalog:item", args=[kwargs.get("pk")])
                )

            error(self.request, "Пустой комментарий")
            return redirect(reverse("catalog:item", args=[kwargs.get("pk")]))

        error(self.request, "Вы не вошли в аккаунт")
        return redirect(reverse("person:login"))

    @staticmethod
    def check_length_comment(comment):
        if validate_space_len_comment(comment) and validate_length_comment(
            comment
        ):
            return True
        return False

    @staticmethod
    def add_comment(comment, user, film_id):
        Comment.objects.create(user=user, comment=comment, film_id=film_id)
