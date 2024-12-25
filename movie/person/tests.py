from django.test import TestCase, Client
from django.urls import reverse
from parameterized import parameterized
from http import HTTPStatus


class RegistrationTest(TestCase):
    def setUp(self):
        super().setUp()
        self.login_user = Client()
        user_data = {
            "username": "Orneys1",
            "password": "qazwsxedc123",
            "repeat_password": "qazwsxedc123",
            "email": "georgijsavin17122@gmail.com",
            "image": "",
            "birthday": "2006-02-17",
        }
        self.login_user.post(
            path=reverse("person:registration"), data=user_data
        )
        self.login_user.login(
            username=user_data.get("username"),
            password=user_data.get("password"),
        )

        self.registered_user = Client()
        user_data = {
            "username": "Orneys2",
            "password": "qazwsxedc123",
            "repeat_password": "qazwsxedc123",
            "email": "sawingeorgiy@gmail.com",
            "image": "",
            "birthday": "2006-02-17",
        }
        self.registered_user.post(
            path=reverse("person:registration"), data=user_data
        )
        self.registered_user.logout()

    @parameterized.expand(
        [
            (
                {
                    "username": "Orneys1",
                    "password": "qazwsxedc123",
                    "repeat_password": "qazwsxedc123",
                    "email": "sawingeorgiy@gmail.com",
                    "image": "",
                    "birthday": "2006-02-17",
                },
                HTTPStatus.FOUND,
                reverse("person:registration"),
            ),
        ]
    )
    def test_registration_form_post(self, data, status_code, url):
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
    def test_registration_form_get(self, status_code):
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
    def setUp(self):
        super().setUp()
        self.login_user = Client()
        user_data = {
            "username": "Orneys1",
            "password": "qazwsxedc123",
            "repeat_password": "qazwsxedc123",
            "email": "georgijsavin17122@gmail.com",
            "image": "",
            "birthday": "2006-02-17",
        }
        self.login_user.post(
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


class ProfileTest(TestCase):
    def setUp(self):
        super().setUp()
        self.login_user = Client()
        user_data = {
            "username": "Orneys1",
            "password": "qazwsxedc123",
            "repeat_password": "qazwsxedc123",
            "email": "georgijsavin17122@gmail.com",
            "image": "",
            "birthday": "2006-02-17",
        }
        self.login_user.post(
            path=reverse("person:registration"), data=user_data
        )

    @parameterized.expand(
        [
            (
                {
                    "username": "Orneys2",
                    "email": "123savin@gmail.com",
                    "image": "",
                    "birthday": "1999-12-12",
                },
            ),
        ]
    )
    def test_change_profile(self, data):
        self.login_user.post(path=reverse("person:profile"), data=data)
        response = self.login_user.get(path=reverse("person:profile"))
        content = response.content.decode()
        self.assertIn(data.get("username"), content)
        self.assertIn(data.get("email"), content)
        self.assertIn("Dec. 12, 1999", content)
