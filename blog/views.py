from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView
from .models import Post
from .forms import PostForm

# Create your views here.


class BlogView(View):
    def get(self, request):
        all_posts = Post.objects.all()
        return render(request, "home.html", {"all_posts": all_posts})


class BlogCreateView(View):
    template_name = "post_new.html"

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, self.template_name, {"form": form})


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogUpdateView(View):
    template_name = "post_edit.html"

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(instance=post)
        return render(request, self.template_name, {"form": form, "post": post})

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, self.template_name, {"form": form, "post": post})


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
