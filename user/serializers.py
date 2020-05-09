from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from user.models import City, Cleaner, Customer, Appointment


class CitySerializers(serializers.ModelSerializer):
    class Mete:
        model = City
        fields = '__all__'


class CleanerSerializers(serializers.ModelSerializer):
    class Mete:
        model = Cleaner
        fields = '__all__'


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class AppointmentSerializers(serializers.ModelSerializer):
    phone_number = PhoneNumberField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date = serializers.DateField()
    time = serializers.DateField()
    city = serializers.PrimaryKeyRelatedField(queryset = City.objects.filter(is_able = True))
