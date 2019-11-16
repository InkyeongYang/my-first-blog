from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter(author=User.objects.get(username='admin'))
    return render(request, 'blog/post_list.html', {'posts' : posts})
