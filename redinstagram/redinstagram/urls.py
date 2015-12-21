from django.conf.urls import url, include
from django.contrib import admin

from redinstagram.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include([
        url(r'^facebook/$', FacebookPageRedirectView.as_view(), name='page'),
        url(r'^facebook/message/$', FacebookMessageRedirectView.as_view(), name='message'),
        url(r'^contact/$', FacebookMessageRedirectView.as_view(), name='contact'),
    ], namespace='facebook')),

    url(r'^tags/', include([
        url(r'^(?P<slug>\w+)/$', HashtagDetailView.as_view(), name='detail'),
    ], namespace='hashtag')),

    url(r'^posts/', include([
    ], namespace='post')),
]
