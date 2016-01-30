from django.conf.urls import url, patterns
from api.views import MovieListView

urlpatterns = [
    url(r'^movies/', MovieListView.as_view(), name='movie_list'),
]
