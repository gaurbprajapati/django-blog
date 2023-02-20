from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (

    ListView, DetailView, CreateView,
    UpdateView,
    DeleteView
)

# from django.http import HttpResponse

from .models import Post

from django import forms


# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    # giving the model form which it queury the data
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html

    context_object_name = 'posts'

# sorting the post on the bases of date post
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

    '''
    we have tow option to use template 
    1.-make template with   #<app>/<model>_<viewtype>.html exp. post_detail.html that we are using 
    2. use template by name as we are used in above class PostListView 
    '''
    # template_name = "TEMPLATE_NAME"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

# orriding the mdethod from_valid to give the auther of the form is user
    def form_valid(self, forms):
        forms.instance.auther = self.request.user
        return super().form_valid(forms)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
# this is will check that other people is not able to update the other post
# if this function and UserPassesTestMixin will not there then anyone can update anyone post

    def test_func(self):
        post = self.get_object()
        if (self.request.user) == post.auther:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    # template_name = "TEMPLATE_NAME"

    def test_func(self):
        post = self.get_object()
        if (self.request.user) == post.auther:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# def register(request):
#     return render(request, "users/register.html")
