"""
URL configuration for friender project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import  include, path
from . import views

from .views import (
    # some_view,
    # MyView,
    # some_template_view,
    home_view,
    hotels_view,
    users_view,
    user_comment_view,
    book_room,
    hotel_comment_add_form,
    # persons_view,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    # path('venues/', views.venues, name='venues'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('home', home_view, name="home"),
    path('hotels', hotels_view, name="hotels"),
    path('users', users_view, name="users"),
    path('user_comment', user_comment_view, name="user_comment"),
    path('book/<str:hotel_name>/<int:user_id>/<str:room_number>/',  book_room, name='book_room'),
    path('create_user/', views.create_user, name='create_user'),
    path('comment_add', hotel_comment_add_form, name="comment_add"),
]
