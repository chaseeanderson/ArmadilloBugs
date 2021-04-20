from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubscriberCreate.as_view(), name='home'),
    path('confirm/<int:subscriber_id>', views.confirm, name='confirm'),
    path('index/', views.index),
]