from django.test import TestCase, Client
from django.urls import reverse
from parameterized import parameterized
from http import HTTPStatus

from catalog.models import Film


class CatalogTest(TestCase):
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
            HTTPStatus.OK,
        ]
    )
    def test_catalog_get_login_user(self, status_code):
        response = self.login_user.get(path=reverse("catalog:catalog"))
        self.assertEqual(response.status_code, status_code)

    @parameterized.expand(
        [
            (HTTPStatus.FOUND, reverse("person:login")),
        ]
    )
    def test_catalog_get_unlogin_user(self, status_code, url):
        self.login_user.logout()
        response = self.login_user.get(path=reverse("catalog:catalog"))
        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.url, url)


class ItemTest(TestCase):
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
        cls.film = Film.objects.create(
            id=1,
            name="Film1",
            description="Film1",
            image="",
            year_of_release=2020,
            premiere="2020-12-12",
            country="USA",
            movie="",
            mark=10,
            is_eighteen=True,
            director="Director",
        )
        cls.unlogin_user = Client()
        user_data = {
            "username": "Orneys1",
            "password": "qazwsxedc123",
            "repeat_password": "qazwsxedc123",
            "email": "georgijsavin17122@gmail.com",
            "image": "",
            "birthday": "2006-02-17",
        }
        cls.unlogin_user.post(
            path=reverse("person:registration"), data=user_data
        )
        cls.unlogin_user.logout()

    @parameterized.expand(
        [
            HTTPStatus.OK,
        ]
    )
    def test_item_get_login_user(self, status_code):
        response = self.login_user.get(
            path=reverse("catalog:item", args=[self.film.id])
        )
        self.assertEqual(response.status_code, status_code)

    @parameterized.expand(
        [
            (HTTPStatus.FOUND, reverse("person:login")),
        ]
    )
    def test_item_get_unlogin_user(self, status_code, url):
        response = self.unlogin_user.get(
            path=reverse("catalog:item", args=[self.film.id])
        )
        self.assertEqual(response.status_code, status_code)
        self.assertRedirects(response, url)
