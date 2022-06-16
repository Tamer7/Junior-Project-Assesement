from django.test import TestCase
from django.urls import reverse


from .models import Booking



class AppViewTests(TestCase):
    """

    Checking if Commision rate is as requirements
    June to September - 15%
    Other Months - 10%
    
    """
    def setUp(self):

        Booking.objects.create(date="2022-05-20")
        Booking.objects.create(date="2022-06-20")
        Booking.objects.create(date="2022-07-20")
        Booking.objects.create(date="2022-08-20")
        Booking.objects.create(date="2022-09-20")

    def test_month_true(self):
        may = Booking.objects.get(date="2022-05-20")
        june = Booking.objects.get(date="2022-06-20")
        july = Booking.objects.get(date="2022-07-20")
        august = Booking.objects.get(date="2022-08-20")
        september = Booking.objects.get(date="2022-09-20")

        self.assertEqual(Booking.CalculateCommision(may), 10.0)
        self.assertEqual(Booking.CalculateCommision(june), 15.0)
        self.assertEqual(Booking.CalculateCommision(july), 15.0)
        self.assertEqual(Booking.CalculateCommision(august), 15.0)
        self.assertEqual(Booking.CalculateCommision(september), 15.0)


   