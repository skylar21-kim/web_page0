from django.views.generic import ListView, DetailView
from . models import Post

# Create your views here.
class PostList(ListView) :
    model = Post
    ordering = '-pk'

# Post 상세 보기
class PostDetail(DetailView) :
    model = Post