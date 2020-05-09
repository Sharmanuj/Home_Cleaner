from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from user.serializers import CitySerializers, CleanerSerializers, CustomerSerializers, AppointmentSerializers
from user.models import City, Cleaner, Customer, Appointment

class CityView(viewsets.ModelViewSet):
    queryset = City.objects.filter(is_able = True)
    serializer_class = CitySerializers


class CleanerView(viewsets.ModelViewSet):
    queryset = Cleaner.objects.filter()
    serializer_class = CleanerSerializers


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.filter()
    serializer_class = CustomerSerializers

class AppointmentCreateView(CreateAPIView):
    serializer_class = AppointmentSerializers

    def create(self, request, *args, **kwargs):
        serializer  = self.get_serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            phone_number = serializer.validated_data.get('phone_number')
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer._validated_data.get('last_name')
            date = serializer.validated_data.get('date')
            time = serializer.validated_data.get('time')

            cust = Customer.objects.filter(phone_number = phone_number).first()
            if not cust:
                cust = Customer.objects.create(phone_number=phone_number,first_name=first_name,last_name=last_name,city_id = city_id)
                cust.save()
            city_cleaner = Cleaner.objects.filter(city_id=city).values_list('id')
            available_cleaner = Appointment.objects.filter(cleaner__city_id = city.id, date = date, time = time).values_list('cleaner')
            free_cleaner = set(city_cleaner) - set(available_cleaner)
            if free_cleaner:
                cleaner = free_cleaner.pop()[0]
                appointment = Appointment.objects.create(customer = cust, cleaner_id = cleaner, date = date, time = time)
                msg = {'message': "appointment has been accepted by {}".format(appointment.cleaner)}
