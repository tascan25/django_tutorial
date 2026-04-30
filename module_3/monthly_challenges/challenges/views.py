from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

challenge_texts = {
        "january":"Eat no meat for the entire month",
        "february":"Walk for at least 20 minutes every day",
        "march":"Learn Django for at least 20 minutes every day",
        "april":"Eat no meat for the entire month",
        "may":"Walk for at least 20 minutes every day",
        "june":"Learn Django for at least 20 minutes every day",
        "july":"Eat no meat for the entire month",
        "august":"Walk for at least 20 minutes every day",
        "september":"Learn Django for at least 20 minutes every day",
        "october":"Eat no meat for the entire month",
        "november":"Walk for at least 20 minutes every day",
        "december":"Learn Django for at least 20 minutes every day",
    }



def index(request):
    month_tag = []
    months = list(challenge_texts.keys())
    for month in months:
        capitalize_month = month.capitalize()
        redirect_path = reverse('monthly-challenge',args=[month])
        month_tag.append(f"<li><a href='{redirect_path}'>{capitalize_month}</a></li>")
    response_data = f"<ul> {
        ''.join(month_tag)
    }</ul>" 
    return HttpResponse(response_data)

def monthly_challenges_number(request,month):
    try:
        months_list = list(challenge_texts.keys())
        redirect_month = months_list[month-1]
        redirect_path = reverse("monthly-challenge",args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except IndexError:
        return HttpResponseNotFound("invalid request")

def monthly_challenge(request, month):
    try:
        returned_html = f'<h1>{challenge_texts[month]}</h1>'
        return HttpResponse(returned_html)
    except KeyError:
        return HttpResponseNotFound("This month is not supported")