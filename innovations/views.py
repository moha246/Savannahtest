from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Post
from .forms import CommentForm


# Create your views here.
def index(request):
    return render(request, "innovations/index.html", {"name": "Home"})


def about(request):
    return render(request, "innovations/about.html", {"name": "about"})


def our_team(request):
    return render(request, "innovations/our_team.html", {"name": "our_team"})


def tataafo(request):
    return render(request, "innovations/tataafo.html", {"name": "tatafoo"})


def fitzone(request):
    return render(request, "innovations/fitzone.html", {"name": "fitzone"})


def hacby(request):
    return render(request, "innovations/hacby.html", {"name": "hacby"})


def sTrac(request):
    return render(request, "innovations/sTrac.html", {"name": "sTrac"})


def contact(request):
    return render(request, "innovations/contact.html", {"name": "contact"})


def data_science(request):
    return render(request, "innovations/data_science.html", {"name": "data_science"})


# def blog(request):
#     return render(request, "innovations/blog.html", {})
def public_health(request):
    return render(request, "innovations/public_health.html", {"name": "public_health"})


def software_development(request):
    return render(request, "innovations/software_development.html", {"name": "software_development"})


# def blog_list(request):
#     return render(request, "innovations/blog_list.html", {})


class AllhomeView(ListView):
    template_name = "innovations/home5.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

    def home5(self):
        return render(self, "innovations/home5.html", {"name": "software_development"})


class AllPostsView(ListView):
    template_name = "innovations/blog.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class SinglePostView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "innovations/blog_list.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "innovations/blog_list.html", context)
