from .models import Orders
from django.forms import ModelForm, TextInput, Textarea, Select


class ProductForm(ModelForm):
    class Meta:
        model = Orders
        fields = ["created", "service"]
        widgets = {
            "created": TextInput(attrs={
                'class': 'form-control',
                'type': 'date'

            }),
            "service": Select(attrs={
                'class': 'form-controls',
                'type': 'text'
            }),
        }