from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Contact

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

        labels = {
            "email": _("Your email"),
            "subject": _("Title"),
            "message": _("Your message"),
        }
