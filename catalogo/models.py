from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	

	def __str__(self):
		return self.user.username
def Create_User_Profile(sender, instace, created, **kwargs):
	if created:
		Profile.objects.created(user=instance)

def Save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

		
class Producto(models.Model):
    
	title = models.CharField(max_length=200)  
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the game')
	price = models.IntegerField('Price', default=0 ,help_text='Enter the price of the game in clp$')
	image = models.ImageField()


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this game."""
		return reverse('product-detail', args=[str(self.id)])

		
class Developer(models.Model):
	"""Model representing a developer."""
	name = models.CharField(max_length=100)

	def __str__(self):
		"""String for representing the Model object."""
		return self.name

