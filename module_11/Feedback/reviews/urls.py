from django.urls import path
from . import views
urlpatterns = [
    # path('',views.index,name="starting_page"),
    path('',views.ReviewView.as_view(),name="starting_page"),
    path('thankyou/<str:name>/',views.thank_you)
]
