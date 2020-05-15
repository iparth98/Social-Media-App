from django.urls import path
from . import views
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostDeleteView,
    PostUpdateView,
    UserPostListView,
)


urlpatterns = [
    path("", PostListView.as_view(), name="home-blog"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("about/", views.about_view, name="about-blog"),
]
