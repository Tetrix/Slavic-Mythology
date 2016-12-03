from django import forms
from stories.models import Legends_and_traditions


class Legends_and_traditions_form(forms.ModelForm):
	class Meta:
		model = Legends_and_traditions
		# fields = ('title', 'story')
		exclude = ('user',)