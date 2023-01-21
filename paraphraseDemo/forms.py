from django.forms import ModelForm
from .models import PromptText
from django import forms


class PromptTextForm(ModelForm):
    class Meta:
        model=PromptText
        fields="__all__"
        
        widgets = {
            'prompt_text': forms.Textarea(
                attrs={'placeholder': 'Enter your prompt'}),
            

        }
