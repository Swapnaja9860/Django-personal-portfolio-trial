from django.shortcuts import render,get_object_or_404
from .models import subproject_blog

# Create your views here.

def all_blogs(request):
	subproject_blogs = subproject_blog.objects.order_by('-date')[:4];
	return render(request , 'blog/home.html' , { 'subproject_blogs' : subproject_blogs} );

def detail(request , blog_id):
	sub = get_object_or_404(subproject_blog, pk=blog_id)
	return render(request , 'blog/detail.html' , {'sub' : sub});
