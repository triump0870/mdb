from django.conf.urls import url, patterns, include
from api.views import MovieListView, MovieDetailView, UserListView, UserDetailView, api_root
from .views import UserViewSet, MovieViewSet
from rest_framework.routers import DefaultRouter


# Create a router and register the viewsets with it
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'users', UserViewSet)


# movie_list = MovieViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# movie_detail = MovieViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^$', api_root, name='api-root'),
    # url(r'^movies/', movie_list, name='movie-list'),
    # url(r'^movies/(?P<pk>.+)/$', movie_detail, name='movie-detail'),
    # url(r'^users/$',user_list, name='user-list'),
    # url(r'^users/(?P<pk>.+)/$', user_detail, name='user-detail'),
]
