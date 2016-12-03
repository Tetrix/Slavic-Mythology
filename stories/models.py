from django.db import models
from home.models import UserProfile
from django.contrib.auth.models import User

class Legends_and_traditions(models.Model):
	user = models.ForeignKey(User, null=True)
	title = models.CharField(max_length = 100, null=True)
	story = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.title

