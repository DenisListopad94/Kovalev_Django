from django.http import HttpRequest, HttpResponse,  HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from .forms import UserModelForm, HotelsCommentForm
from django.shortcuts import render
from django.urls import reverse,  reverse_lazy
from datetime import datetime,  timedelta
from django.db import transaction
from .models import  Hotels, Persons, Room, Booking, User, PersonComment


def current_datetime(request):
    now = datetime.now().date()
    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)

def home(request):
    html = "<html><body><p>Dating Site Rules</p> <ul> <li>Be honest in your profile information.</li> <li>Respect other users’ boundaries and privacy.</li> <li>Do not harass or send unsolicited messages.</li> <li>Use appropriate language and be respectful in your communication.</li> <li>Do not share personal contact information too soon.</li> <li>Report any suspicious or inappropriate behavior to the site administrators.</li> <li>Be patient and open-minded when getting to know someone.</li> <li>Remember that not everyone will be a perfect match, and that’s okay.</li> <li>Have fun and enjoy the process of meeting new people!</li></body></html>"
    return HttpResponse(html)

def venues(request):
    html = "<html><body><p>List of establishments</p><ul><li>Empty at the moment</ul></body></html>" 
    return HttpResponse(html)

class Home_view(TemplateView):
    template_name="home.html"

def hotels_view(request):
    context = {
        "hotels": Hotels.objects.prefetch_related("hotel_comments").all()
    }
    return render(request=request,
                  template_name="hotels.html",
                  context=context
                  )



class Users_view(ListView):
    model = User
    template_name="users.html"
    context_object_name = "users"
    paginate_by = 4

class UserDetailView(DetailView):
    model = User
    template_name = "user-detail.html"
    context_object_name = "users"

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return User.objects.get(id=id)

def user_comment_view(request):
    context = {
        "persons": Persons.objects.prefetch_related("person_comments").all()
    }
    return render(
        request=request,
        template_name="user_comments.html",
        context=context
    )

@transaction.atomic
def book_room(request, hotel_name, user_id, room_number):
    if request.method == 'POST':
        try:
            hotel = Hotels.objects.get(name=hotel_name)
        except Hotels.DoesNotExist:
            return HttpResponse('Hotel with this name not exist', status=404)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return HttpResponse('User with this ID not exist', status=404)

        try:
            room = Room.objects.get(hotel=hotel, number=room_number)
        except Room.DoesNotExist:
            return HttpResponse('Room with this number not exist in this hotel', status=404)

        if room.is_booked:
            return HttpResponse('This room is booked', status=400)

        room.is_booked = True
        room.save()

        booking = Booking(
            room=room,
            start_date=datetime.now().date(),
            end_date=datetime.now().date() + timedelta(days=7) ,
            customer_full_name=f"{user.first_name} {user.last_name}"
        )
        booking.save()

        return HttpResponse('Room successfully booked')

    return render(
        request,
        'booking.html',
        {
            'hotel_name': hotel_name,
            'user_id': user_id,
            'room_number': room_number
        }
    )

class Create_user(CreateView):
    model = User
    form_class = UserModelForm
    template_name = 'create_user.html'  
    success_url = '/users'  

    def form_valid(self, form):
        return super().form_valid(form)


class HotelCommentFormView(FormView):
    template_name = "add_comments.html"
    form_class = HotelsCommentForm
    success_url = reverse_lazy("hotels")

# hotels = [
#     {
#         "name":"Plaza",
#         "address":"LosAngeles",
#         "stars":5
#     },
#     {
#         "name":"Turist",
#         "address":"Minsk",
#         "stars":4
#     },
#     {
#         "name":"Bungalo",
#         "address":"Ghana",
#         "stars":2
#     },
# ]

# users = [
#     {
#         "name": "John",
#         "age": 40,
#         "comment" : ["some John comment", "another John comment"],
#         "photo" :  'static/john.jpg',
#     },
#     {
#         "name": "Ann",
#         "age": 28,
#         "comment": ["some Ann comment", "another Ann comment"],
#         "photo" :  'static/ann.jpg',
#     },
#     {
#         "name": "Peter",
#         "age": 18,
#         "comment": ["some Peter comment", "another Peter comment"],
#         "photo" :  'static/peter.jpg'
#     },
# ]



