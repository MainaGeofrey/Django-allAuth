


from django.urls import path
from userAuth import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
