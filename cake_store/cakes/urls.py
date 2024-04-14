from django.urls import path
from .views import home_page, index_page, cake_details

urlpatterns = [
    path('', home_page),
    path('index/', index_page),
    path('details/<int:pk>/', cake_details)
]