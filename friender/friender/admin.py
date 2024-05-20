from .models import Person, Profile, Hotels, HotelsComment, Book_order_info, Hobbies, Hotel_owner

from django.contrib import admin

admin.site.register(Person)
admin.site.register(Profile)
admin.site.register(Hotels)
admin.site.register(HotelsComment)
admin.site.register(Book_order_info)
admin.site.register(Hobbies)
admin.site.register(Hotel_owner)