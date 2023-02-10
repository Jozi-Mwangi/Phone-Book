from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email']