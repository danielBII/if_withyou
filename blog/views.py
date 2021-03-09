from django.shortcuts import render

# Create your views here.
from blog.models import Post
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {' posts ': posts})
