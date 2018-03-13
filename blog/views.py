from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.urls import reverse
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

from .models import *



def article_list(request):
	article_list = Article.objects.all()
	ctx = {
		'article_list': article_list,
	}
	return render(request, 'blog/article_list.html', ctx)

def article1(request):
	return render(request, 'blog/article1.html')



def article2(request):
	return render(request, 'blog/article2.html')


def article3(request):
	return render(request, 'blog/article3.html')

def article4(request):
	return render(request, 'blog/article4.html')

def article5(request):
	return render(request, 'blog/article5.html')

def article6(request):
	return render(request, 'blog/article6.html')

def article7(request):
	return render(request, 'blog/movie.html')

def article8(request):
	return render(request, 'blog/crime.html')

