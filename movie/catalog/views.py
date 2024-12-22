from django.shortcuts import render, redirect, reverse
from django.contrib.messages import success, error
from django.views import View

from catalog.models import Film, Genre


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
            }
            return render(self.request, "catalog/item.html", context)

        error(self.request, "Вы не вошли в аккаунт")
        return redirect(reverse("person:login"))

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            pass

        error(self.request, "Вы не вошли в аккаунт")
        return redirect(reverse("person:login"))
