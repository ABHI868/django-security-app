from django.db import models
from django.urls import reverse
# Create your models here.
class Visitors(models.Model):
    Name=models.CharField(max_length=70)
    Address=models.CharField(max_length=300)
    Telephone=models.IntegerField()
    Email=models.EmailField()
    purpose=models.TextField(max_length=500)    
    checkin=models.IntegerField()
    checkout=models.IntegerField()

class security(models.Model):
	name=models.CharField(max_length=80)
	band=models.CharField(max_length=50)
	contact_no=models.IntegerField()

class maintenance(models.Model):
	name=models.CharField(max_length=80)
	email=models.EmailField()
	availability=models.BooleanField(default=False)

class Public(models.Model):
	name=models.CharField(max_length=70)
	contact=models.IntegerField()

	def get_absolute_url(self):
		return reverse("Sangaria:home")



