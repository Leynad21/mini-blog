from django.shortcuts import render
from django.views import View

from .models import Post

# Create your views here.


class BlogView(View):
    def get(self, request):
        all_posts = Post.objects.all()
        print(all_posts)
        return render(request, "home.html")
