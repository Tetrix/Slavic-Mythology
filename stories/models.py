from django.db import models
from home.models import UserProfile

class Legends_and_traditions(models.Model):
	form = models.ForeignKey(UserProfile)
	title = models.CharField(max_length = 100, null=True)
	story = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.title

