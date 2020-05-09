from django.urls import path
from rest_framework import routers
from user.views import CityView, CleanerView, CustomerView, AppointmentCreateView

routers = routers.SimpleRouter()
routers.register('city', CityView, 'city')
routers.register('cleaner', CleanerView, 'cleaner')
routers.register('customer', CustomerView, 'customer')


urlpatterns = [
    path('appointment', AppointmentCreateView.as_view(), 'appointment'),
]
urlpatterns += routers.urls
