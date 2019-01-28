# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class UserProfileInfo(models.Model):

   # user = models.OneToOneField(User,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
   # password = models.OneToOneField(User,on_delete=models.CASCADE)
    
def __str__(self):
  return self.user.username

class Product(models.Model):
    p_k = models.IntegerField(primary_key=True)
    item= models.TextField(max_length=2000)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to = 'static/expenses/',null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.item) + ": Rs" + str(self.price)

    def get_absolute_url(self):
        return reverse('itemupdate', kwargs={'pk': self.p_k})
