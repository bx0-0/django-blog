from typing import Any
from django.forms import BaseModelForm
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseForbidden
from .models import Post,Comment 
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm, DeleteConfirmationForm ,UpdatePostForm
from django.views.generic.edit import FormMixin
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(decorator=login_required,name='post')
class PostDetailView(DetailView,FormMixin):
    form_class = CommentForm
    http_method_names = ['get', 'post']
    model = Post
    template_name = "single_blog/post_detail.html"
    context_object_name = 'post'
    success_url = '#'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comment = Comment.objects.filter(post = post)
        context.update({'comment':comment})
        
        return context
    
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.post = self.get_object()
        form.instance.user = self.request.user
        profile = Profile.objects.get(user=self.request.user)
        form.instance.profile = profile
        print(form)

        form.save()
        return super().form_valid(form)
        
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "single_blog/add_post.html"
    fields = ['title', 'description','PostImg']
    @transaction.atomic
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        slug = self.object.slug
        url  = f'../{slug}/'
        return url


class YourPostsListView(LoginRequiredMixin,ListView,FormMixin):
    model = Post
    template_name = "single_blog/my_posts.html"
    paginate_by = 6
    context_object_name = 'posts'
    form_class = DeleteConfirmationForm
    success_url = '../../post/my-posts'
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-create_at')
    
    
    def post(self,request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            print("Validating")

            return self.form_invalid(form)
    def form_valid(self, form: Any) -> HttpResponse:
        slug = form.cleaned_data.get('slug')
        try:
            obj = Post.objects.get(slug=slug)

        except Post.DoesNotExist:
            return Http404("No such post")
        if self.request.user.is_authenticated and obj.user == self.request.user:
            obj.delete()
            
        return super().form_valid(form)  

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "single_blog/update_post.html"
    success_url = '../my-posts'
    form_class = UpdatePostForm

    def form_valid(self, form: Any) -> HttpResponse:
        try:
            obj = self.get_object()

        except Post.DoesNotExist:
            return Http404("No such post exists")
        if self.request.user.is_authenticated and obj.user == self.request.user:
            return super().form_valid(form)  
        else:
            
            return HttpResponseForbidden("You do not have permission to update this post.")
            

    