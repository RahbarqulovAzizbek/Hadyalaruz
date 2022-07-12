from django import forms
from django.forms.models import ModelForm
from .models import CommentModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['post', 'created_at']