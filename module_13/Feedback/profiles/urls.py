from django.urls import path
from . import views

urlpatterns = [
    # path("", views.CreateProfileView.as_view())
    path("", views.CreateProfileViewUsingCreateView.as_view()),
    path("list/",views.ProfileViews.as_view())
]