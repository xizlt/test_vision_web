from django.core.mail import send_mail

from .tasks import sent_message
from rest_framework import serializers
from content.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['name', 'email']

    def create(self, validated_data):
        message = Message.objects.create(**validated_data)
        send_mail("New order", f"new oder from {validated_data.get('name')} ", 'from@example.com',
                  [validated_data.get('email')])
        # sent_message.delay(email=validated_data.get('email'), name=validated_data.get('name'))
        return message
