from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def post_create(request):
	return HttpResponse('<h1> Create </h1>')

def post_detail(request, slug):
	return HttpResponse("<h1> {0} </h1>".format(slug))

def post_update(request, slug):
	return HttpResponse('<h1> Update </h1>')
	
def post_delete(request, slug):
	return HttpResponse('<h1> Delete </h1>')
	
def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'posts/index.html', context)
