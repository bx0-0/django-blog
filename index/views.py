from single_blog.models import Post
from django.views.generic.list import ListView
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "index/home.html"
    context_object_name = 'posts'
    ordering = ['-create_at']
    paginate_by = 4