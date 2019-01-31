from django.shortcuts import render
from .models import blockPost

# Create your views here.


def HomePage(request):
	postData = blockPost.objects.all()
	return render(request,'index.html', context = {'data': postData})


def post_detail(request, title):
	post = blockPost.objects.get(title__iexact=title)
	return render(request, 'post_detail.html', context={'post':post})