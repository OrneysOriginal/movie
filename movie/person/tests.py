from django.test import TestCase, Client
from django.urls import reverse
from parameterized import parameterized
from http import HTTPStatus


class RegistrationTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.login_user = Client()
        user_data = {
            "username": "Orneys1",
            "password": "qazwsxedc123",
            "repeat_password": "qazwsxedc123",
            "email": "georgijsavin17122@gmail.com",
            "image": "",
            "birthday": "2006-02-17",
        }
        cls.login_user.post(
            path=reverse("person:registration"), data=user_data
        )
        cls.login_user.login(
            username=user_data.get("username"),
            password=user_data.get("password"),
        )

        cls.registered_user = Client()
        user_data = {
            "username": "Orneys2",
            "password": "qazwsxedc123",
            "repeat_password": "qazwsxedc123",
            "email": "sawingeorgiy@gmail.com",
            "image": "",
            "birthday": "2006-02-17",
        }
        cls.registered_user.post(
            path=reverse("person:registration"), data=user_data
        )
        cls.registered_user.logout()

    @parameterized.expand(
        [
            (
                {
                    "username": "Orneys1",
                    "password": "qazwsxedc123",
                    "repeat_password": "qazwsxedc123",
                    "email": "savingeorgiy@yandex.ru",
                    "image": "",
                    "birthday": "2006-02-17",
                },
                HTTPStatus.FOUND,
                reverse("person:registration"),
            ),
        ]
    )
    def test_registration_form_registration_user(self, data, status_code, url):
        response = self.registered_user.post(
            path=reverse("person:registration"), data=data
        )
        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.url, url)

    @parameterized.expand(
        [
            HTTPStatus.OK,
        ]
    )
    def test_registration_form_registration_user(self, status_code):
        response = self.registered_user.get(
            path=reverse("person:registration")
        )
        self.assertEqual(response.status_code, status_code)

    @parameterized.expand(
        [
            (
                {
                    "username": "Orneys4",
                    "password": "qazwsxedc123",
                    "repeat_password": "qazwsxedc123",
                    "email": "savingeorgiy@yandex.ru",
                    "image": "",
                    "birthday": "2006-02-17",
                },
                HTTPStatus.FOUND,
                reverse("person:profile"),
            ),
        ]
    )
    def test_registration_form_login_user(self, data, status_code, url):
        response = self.login_user.post(
            path=reverse("person:registration"), data=data
        )
        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.url, url)


class LoginTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.login_user = Client()
        user_data = {
            "username": "Orneys1",
            "password": "qazwsxedc123",
            "repeat_password": "qazwsxedc123",
            "email": "georgijsavin17122@gmail.com",
            "image": "",
            "birthday": "2006-02-17",
        }
        cls.login_user.post(
            path=reverse("person:registration"), data=user_data
        )

    @parameterized.expand(
        [
            (
                {"username": "Orneys1", "password": "qazwsxedc123"},
                HTTPStatus.FOUND,
                reverse("person:profile"),
            ),
        ]
    )
    def test_login_form_login_user(self, data, status_code, url):
        response = self.login_user.post(
            path=reverse("person:login"), data=data
        )
        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.url, url)
