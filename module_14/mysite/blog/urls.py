from django.urls import path 
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(),name="starting_page"),
    path("posts/",views.PostListView.as_view(),name="posts_page"),
    path("posts/<slug:slug>",views.PostDetailView.as_view(),name="posts_detail_page"),
    path("blog/entry",views.BlogEntryView.as_view(),name="blog_entry"), 
    path('read-later', views.ReadLaterView.as_view(),name="read_later")
]
