from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView,DetailView,FormView
from django.urls import reverse_lazy
from django.views.generic import UpdateView,DeleteView
from django.views.generic import CreateView


from . import models
from . import froms


class PostListView(LoginRequiredMixin, ListView, FormView):

    model=models.Post
    form_class=froms.CommentReplyForm
    success_url='/posts/'
    template_name='post_list.html'
    login_url='login'

    


class PostDetailView(LoginRequiredMixin, DetailView):
    model=models.Post
    template_name='post_detail.html'
    login_url = 'login'



class PostUpdateView(LoginRequiredMixin,UpdateView):
    model=models.Post

    fields=['message']
    template_name='post_edit.html'
    login_url='login'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model=models.Post
    template_name='post_delete.html'
    success_url=reverse_lazy('post_list')
    login_url='login'


class PostCreateView(LoginRequiredMixin, CreateView):
    model=models.Post
    template_name='post_new.html'
    fields=['message']
    success_url = reverse_lazy('post_list')
    login_url='login'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
