from django.views.generic.detail import DetailView

from redinstagram.models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'
    slug_field = 'hash_id'
