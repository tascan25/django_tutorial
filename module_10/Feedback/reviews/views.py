from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForms


def index(request):
    if request.method == 'POST':
        entered_username = request.POST['user_name']
        form = ReviewForms(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect(f"/thankyou/{entered_username}")
    else:
        form = ReviewForms()
        return render(request, 'reviews/review.html',{
            "form":form
        })


def thank_you(request, name):
    return render(request, 'reviews/thank_you.html', {
        "name": name
    })