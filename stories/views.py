from django.shortcuts import render


def index(request):
	return render(request, 'stories/index.html')

def write_story(request):
	return render(request, 'stories/write_story.html')	