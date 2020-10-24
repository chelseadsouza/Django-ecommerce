from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	item = models.CharField(max_length=100)
	amount = models.IntegerField()
	date = models.DateTimeField(default=timezone.now)
	member = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.item


class Details(models.Model):
	Name =  models.CharField(max_length=100)
	Address =  models.CharField(max_length=10000)
	Country =  models.CharField(max_length=100)
	City =  models.CharField(max_length=100)
	Item = models.CharField(max_length=100)
	Phone = models.IntegerField()

	def __str__(self):
		return self.Name

class Contact(models.Model):
	FirstName =  models.CharField(max_length=100)
	LastName =  models.CharField(max_length=10000)
	Email =  models.CharField(max_length=100)
	Subject =  models.CharField(max_length=100)
	Message =  models.CharField(max_length=100)


	def __str__(self):
		return self.FirstName


