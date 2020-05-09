from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class City(models.Model):
    city_name = models.CharField(max_length = 50, unique = True)
    is_able = models.BooleanField(default = True)
    def __str__(self):
        return self.city_name

class Cleaner(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    city = models.ForeignKey(City, on_delete = models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "{} {}" .format(self.first_name, self.last_name)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique = True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}" .format(self.first_name, self.last_name)

class Appointment(models.Model):
    customer = models.ForeignKey(Customer, blank = True, null = True, on_delete = models.SET_NULL)
    cleaner = models.ForeignKey(Cleaner, blank = True, null = True, on_delete = models.SET_NULL, related_name='booked_appointment')
    date = models.DateField()
    time = models.TimeField()