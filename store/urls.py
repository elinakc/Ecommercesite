from .views import home , Signup
from django.urls import path

urlpatterns = [
    path('', home ),
    path('Signup/', Signup)
]
