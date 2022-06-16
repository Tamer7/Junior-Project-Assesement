from django.shortcuts import render

# Create your views here.

from .models import Booking
from .forms import BookingModelForm



def index(request):
    if request.method == "POST":
        form = BookingModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error ", form.errors)
    form = BookingModelForm()

    new_obj = Booking.objects.latest('id')

    obj = Booking.CalculateCommision(new_obj)


    return render(request, 'index.html', {'form':form, 'obj':obj, 'date':new_obj})





