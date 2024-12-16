from django.shortcuts import render
from django.views import View
from http.client import HTTPResponse


class CatalogView(View):
    def get(self, *args, **kwargs):
        return HTTPResponse

    def post(self, *args, **kwargs):
        return HTTPResponse
