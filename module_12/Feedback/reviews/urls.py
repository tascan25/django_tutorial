from django.urls import path
from . import views
urlpatterns = [
    # path('',views.index,name="starting_page"),
    path('',views.ReviewView.as_view(),name="starting_page"),
    path('reviews/',views.ReviewsListView.as_view(),name="reviews_page"),
    path('thankyou/<str:name>/',views.ThankYouReview.as_view(),name="thankyou_page"),
    path('review/<int:pk>', views.SingleReviewView.as_view(),name="review_detail")
   
]
