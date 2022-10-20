from django.http import HttpResponse
from django.views.generic import View


class Index(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Hello world")