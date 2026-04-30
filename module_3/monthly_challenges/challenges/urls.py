from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
     path("<int:month>", views.monthly_challenges_number, name="monthly-challenge-number"),
    path("<str:month>",views.monthly_challenge, name="monthly-challenge"),
    #the above implementation is of the dynamic urls, where we can pass the month as a parameter and the view will return the challenge for that month
    # the month parameter is automatically passed to the view function as an argument, we can also specify the type of the parameter by using the following syntax <type:parameter>
    # we can access this parameter in thrview function by ex-> def get_challenge(request,month): pass
   
]

