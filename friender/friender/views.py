from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.db import transaction
import datetime
from .models import  Hotels, Persons, Room, Booking

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)

def home(request):
    html = "<html><body><p>Dating Site Rules</p> <ul> <li>Be honest in your profile information.</li> <li>Respect other users’ boundaries and privacy.</li> <li>Do not harass or send unsolicited messages.</li> <li>Use appropriate language and be respectful in your communication.</li> <li>Do not share personal contact information too soon.</li> <li>Report any suspicious or inappropriate behavior to the site administrators.</li> <li>Be patient and open-minded when getting to know someone.</li> <li>Remember that not everyone will be a perfect match, and that’s okay.</li> <li>Have fun and enjoy the process of meeting new people!</li></body></html>"
    return HttpResponse(html)

def venues(request):
    html = "<html><body><p>List of establishments</p><ul><li>Empty at the moment</ul></body></html>" 
    return HttpResponse(html)

def home_view(request):
    return render(
        request=request,
        template_name="home.html",
    )

def hotels_view(request):
    context = {
        "hotels": Hotels.objects.prefetch_related("hotel_comments").all()
    }
    return render(request=request,
                  template_name="hotels.html",
                  context=context
                  )



def users_view(request):
    context = {
        "users": Persons.objects.all().prefetch_related("hobbies")
    }
    return render(request=request,
                  template_name="users.html",
                  context=context
                  )

def user_comment_view(request):
    context = {
        "users": users
    }
    return render(
        request=request,
        template_name="user_comments.html",
        context=context
    )


hotels = [
    {
        "name":"Plaza",
        "address":"LosAngeles",
        "stars":5
    },
    {
        "name":"Turist",
        "address":"Minsk",
        "stars":4
    },
    {
        "name":"Bungalo",
        "address":"Ghana",
        "stars":2
    },
]

users = [
    {
        "name": "John",
        "age": 40,
        "comment" : ["some John comment", "another John comment"],
        "photo" :  'static/john.jpg',
    },
    {
        "name": "Ann",
        "age": 28,
        "comment": ["some Ann comment", "another Ann comment"],
        "photo" :  'static/ann.jpg',
    },
    {
        "name": "Peter",
        "age": 18,
        "comment": ["some Peter comment", "another Peter comment"],
        "photo" :  'static/peter.jpg'
    },
]



