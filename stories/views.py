from django.shortcuts import render
from stories.forms import Legends_and_traditions_form

def index(request):
	return render(request, 'stories/index.html')

def write_story(request):
	if request.method == 'POST':
		write_story = Legends_and_traditions_form(data=request.POST)
		if write_story.is_valid():
			write_story.save()
		else:
			print("OKKKKKKKKKKKKKKKKKKKKKk")	
	return render(request, 'stories/write_story.html')	