from django.forms import ModelForm
from django.core.validators import validate_email
from django.contrib import messages
from .models import Contact

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
