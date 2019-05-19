from django.shortcuts import render
from .models import Blogger, Blog, Comment
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404

def index(request):
    num_authors=Blogger.objects.count()
    num_blogs=Blog.objects.count()
    num_comments=Comment.objects.count()

    return render(
        request,
        'index.html',
        context={
            'page_title':'Главная',
            'num_blogs':num_blogs,
            'num_comments':num_comments,
            'num_authors':num_authors},
    )

class BlogListView(generic.ListView):
    model = Blog
    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['page_title'] = 'All blogs'
        return context
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Blogger
    def get_context_data(self, **kwargs):
        context = super(BloggerListView, self).get_context_data(**kwargs)
        context['page_title'] = 'All bloggers'
        return context

class BloggerDetailView(generic.DetailView):
    model = Blogger

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment',]

    def get_success_url(self): 
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)
