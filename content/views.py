from django.views.generic import ListView
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView

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


class MessageViewSet(generics.CreateAPIView):
    serializer_class = MessageSerializer


# class MessageViewSet(APIView):
#     template_name = 'index.html'
#     serializer = MessageSerializer
#
#     def get(self, request):
#         serializer = self.serializer
#         return Response({'serializer': serializer})
#
#     def post(self, request):
#         serializer = MessageSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer})

