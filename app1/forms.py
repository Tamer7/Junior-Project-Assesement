from .models import Booking
from django import  forms
from django.contrib.admin.widgets import  AdminDateWidget

class BookingForm(forms.Form):
    date_input = forms.DateField(widget=AdminDateWidget())


class BookingModelForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            "date": AdminDateWidget(),
        }