from django.db import models
from django.urls import reverse

# Create your models here.
class Subscriber(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)

  def get_absolute_url(self):
    return reverse('confirm', kwargs={'subscriber_id': self.id})