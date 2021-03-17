from django import forms

from content.models import Message


class MessageCreateForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['name', 'email']
