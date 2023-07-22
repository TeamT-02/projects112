from django.forms import ModelForm
from .models import Home_Contact


class ContactForm(ModelForm):
    class Meta:
        model = Home_Contact
        fields = '__all__'