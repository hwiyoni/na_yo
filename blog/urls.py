from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^post_i/$', views.post_i, name='post_i'),
    url(r'^post_you/$', views.post_you, name='post_you'),
    url(r'^post_they/$', views.post_they, name='post_they'),
    url(r'^search/$', views.SearchFormView.as_view(), name='search'),
]
