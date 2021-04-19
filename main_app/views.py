from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Subscriber

# Create your views here.
class SubscriberCreate(CreateView):
    model = Subscriber
    fields = '__all__'

def confirm(request, subscriber_id):
    subscriber = Subscriber.objects.get(id=subscriber_id)
    return render('confirm.html', {'subscriber': subscriber})