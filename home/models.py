from django.db import models
import os


    

class Gods(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField()
	god_image = models.ImageField(upload_to = 'photos/', blank=True, null=True)

	def __str__(self):
		return self.name


