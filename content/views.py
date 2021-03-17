from django.shortcuts import redirect
from django.views.generic import ListView
from rest_framework.response import Response

from content.models import *
from content.serializers import MessageSerializer


class MainView(ListView):
    model = BlockTitle
    queryset = BlockTitle.objects.last()
    template_name = "index.html"
    context_object_name = "title"

    def get_context_data(self, **kwargs):
        ctx = super(MainView, self).get_context_data(**kwargs)
        ctx['skills'] = BlockSkill.objects.all()
        ctx['review'] = BlockReviews.objects.last()
        ctx['about'] = BlockAbout.objects.last()
        return ctx


