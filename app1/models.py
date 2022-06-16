from django.db import models

# Create your models here.

class Booking(models.Model):
    date = models.DateField(null=True)

    def CalculateCommision(inputDate):
        inputDate = inputDate.date.month
        commision_10 = [6,7,8,9]

        if inputDate in commision_10:
            return float(15)
        else:
            return float(10)
    



