from django.views.generic.detail import DetailView

from redinstagram.models import Hashtag


class HashtagDetailView(DetailView):
    model = Hashtag
    template_name = 'hashtag/detail.html'
    context_object_name = 'hashtag'
    slug_field = 'name'
