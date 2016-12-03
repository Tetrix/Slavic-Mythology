from django.shortcuts import render
from stories.forms import Legends_and_traditions_form
from django.contrib import messages 


def index(request):
	return render(request, 'stories/index.html')

def write_story(request):
	if request.method == 'POST':
		write_story = Legends_and_traditions_form(data=request.POST)
		if write_story.is_valid():
			story = write_story.save(commit=False)
			story.user = request.user
			story.save()
		else:
			messages.error(request, "Error")
	return render(request, 'stories/write_story.html')	