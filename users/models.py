from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default1.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username}Profile'

	def get_absolute_url(self):
		return reverse('ideas-detail', kwargs={'pk': self.pk})


