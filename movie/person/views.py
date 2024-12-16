from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.messages import success, error

from person.forms import RegistrationForm, LoginForm
from person.models import Profile


class LoginView(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            context = {
                "form": LoginForm(),
                "title": "Вход в аккаунт",
            }
            return render(self.request, "person/login.html", context)

        error(self.request, "Вы уже аутентифицированы")
        return redirect(reverse("person:registration"))

    def post(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            form = LoginForm(self.request or None)
            if form.is_bound:
                user = authenticate(self.request.POST)
                if user is not None:
                    login(self.request, user)
                    success(self.request, "Вы успешно вошли")
                    return

                error(
                    self.request, "Пользователя с таким именем и паролем нет"
                )
                return

            error(self.request, "Заполните форму")
            return

        error(self.request, "Вы уже аутентифицированы")
        return


class RegistrationView(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            context = {
                "form": RegistrationForm(),
                "title": "Регистрация",
            }
            return render(self.request, "person/registration.html", context)

        error(self.request, "Вы уже аутентифицированы")
        return redirect(reverse("person:profile"))

    def post(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            form = RegistrationForm(self.request.POST or None)
            data = self.request.POST
            if form.is_bound:
                if self.check_is_unregistered(data):
                    if data.get("password") == data.get("repeat_password"):
                        user = self.create_and_return_user(self.request.POST)
                        login(self.request, user)
                        success(self.request, "Вы успешно зарегистрировались")
                        return redirect(reverse("catalog:catalog"))

                    error(self.request, "Пароли не совпадают")
                    return redirect(reverse("person:registration"))

                error(self.request, "Такой пользователь уже есть")
                return redirect(reverse("person:registration"))

            error(self.request, "Пожалуйста, заполните форму корректно")
            return redirect(reverse("person:registration"))

        error(self.request, "Вы уже аутентифицированы")
        return redirect(reverse("person:profile"))

    @staticmethod
    def create_and_return_user(data):
        user = User.objects.create_user(
            username=data.get("username"),
            password=data.get("password"),
            email=data.get("email"),
        )
        Profile.objects.create(
            user=user,
            image=data.get("image"),
            birthday=data.get("birthday"),
        )
        return user

    @staticmethod
    def check_is_unregistered(data):
        try:
            User.objects.get(username=data.get("username"))
        except ObjectDoesNotExist:
            return True
        return False


class LogoutView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
            success(self.request, "Вы вышли из аккаунта")
            return redirect(reverse("person:login"))

        error(self.request, "Вы не аутентифицированы")
        return redirect(reverse("person:login"))


class ProfileView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            context = {
                "user": self.request.user,
                "profile": Profile.objects.get(id=self.request.user.id),
            }
            return render(self.request, "person:profile", context)

        error(self.request, "Вы не аутентифицированы")
        return redirect(reverse("person:login"))

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            pass

        error(self.request, "Вы не аутентифицированы")
        return redirect(reverse("person:login"))
