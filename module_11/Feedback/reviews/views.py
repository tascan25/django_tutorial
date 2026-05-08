from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForms
from .models import Reviews
from django.views import View


class ReviewView(View):
    def get(self, request):
        form = ReviewForms()
        return render(request, 'reviews/review.html',{
            "form":form
        })
    def post(self,request):
        existing_form = Reviews.objects.get(pk=1)
        entered_username = request.POST['user_name']
        form = ReviewForms(request.POST, instance=existing_form) 
        '''
        now in the above initialization of the form class, we pass the already gathered form data 
        to the form class, in order to let class validate the form. and if it does find something faulty
        then it will generate the, corresponding errors for us
        '''
        
        if form.is_valid():
            '''
            this is the method, which we are talking about in our above comment, 
            '''
            # review = Reviews(
            #     user_name = form.cleaned_data['user_name'],
            #     review_text = form.cleaned_data['review_text'],
            #     rating = form.cleaned_data['rating']
            # )
            # review.save()

            '''
            now we don not need the above code if we are using the model form in order to create the model form, 
            as while using the model form we can directly call the form.save() and it will automaticaly hanles all the things on 
            it's own.
            '''
            form.save()
            print(form.cleaned_data)
            return HttpResponseRedirect(f"/thankyou/{entered_username}")
        return render(request, 'reviews/review.html',{
            "form":form
        })


def index(request):
    if request.method == 'POST':
        existing_form = Reviews.objects.get(pk=1)
        entered_username = request.POST['user_name']
        form = ReviewForms(request.POST, instance=existing_form) 
        '''
        now in the above initialization of the form class, we pass the already gathered form data 
        to the form class, in order to let class validate the form. and if it does find something faulty
        then it will generate the, corresponding errors for us
        '''
        
        if form.is_valid():
            '''
            this is the method, which we are talking about in our above comment, 
            '''
            # review = Reviews(
            #     user_name = form.cleaned_data['user_name'],
            #     review_text = form.cleaned_data['review_text'],
            #     rating = form.cleaned_data['rating']
            # )
            # review.save()

            '''
            now we don not need the above code if we are using the model form in order to create the model form, 
            as while using the model form we can directly call the form.save() and it will automaticaly hanles all the things on 
            it's own.
            '''
            form.save()
            print(form.cleaned_data)
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