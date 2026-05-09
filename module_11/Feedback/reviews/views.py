from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForms
from .models import Reviews
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView


class ReviewView(FormView):
    form_class = ReviewForms
    template_name = "reviews/review.html"

    def form_valid(self, form):
        form.save()
        self.entered_username = form.cleaned_data['user_name']
        return super().form_valid(form)

    def get_success_url(self):
        return f"/thankyou/{self.entered_username}/"
    
   

class ThankYouReview(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["name"] = kwargs['name']
        return context


class ReviewsListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Reviews

    context_object_name = "reviewData"

    
class SingleReviewView(DetailView):
    template_name = "reviews/SingleReview.html"
    model = Reviews