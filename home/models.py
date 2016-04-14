from django.db import models
from django.contrib.auth.models import User


class Gods(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField()
	god_image = models.ImageField(upload_to = 'photos/', blank=True, null=True)

	def __str__(self):
		return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username