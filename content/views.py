from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from content.models import Block


class MainView(ListView):
    model = Block
    queryset = Block.objects.all()
