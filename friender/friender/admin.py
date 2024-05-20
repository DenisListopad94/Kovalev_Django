from .models import (
    Persons,
    HotelOwner,
    Hotels,
    Hobbies,
    Profile,
    BookOrderInfo,
    HotelsComment,
    User,
    PersonComment)

from django.contrib import admin

class PersonCommentInline(admin.StackedInline):
    model = PersonComment

class HotelsInline(admin.StackedInline):
    model = Hotels

class BookInfoInline(admin.StackedInline):
    model = BookOrderInfo


class HotelsCommentInline(admin.TabularInline):
    model = HotelsComment

class HobbiesInline(admin.TabularInline):
    model = Hobbies.owners.through

class PersonsAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "sex"]
    search_fields = ["first_name", "last_name", "age", "sex"]
    list_filter = ["first_name", "last_name"]
    inlines = [
        PersonCommentInline
    ]
    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name"],
            },
        ),
        (
            "Additional info",
            {
                "classes": ["collapse"],
                "fields": ["age", "sex"],
            },
        ),
    ]


class HotelOwnerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "sex"]
    search_fields = ["first_name", "last_name", "age", "sex"]
    list_filter = ["first_name", "last_name"]
    inlines = [
        HotelsInline
    ]
    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name"],
            },
        ),
        (
            "Additional info",
            {
                "classes": ["collapse"],
                "fields": ["age", "sex"],
            },
        ),
    ]


class HotelsAdmin(admin.ModelAdmin):
    list_display = ["name", "stars", "address", "city", "phone", "owners"]
    search_fields = ["name", "address", "city"]
    list_filter = ["name", "stars", "address", "city"]
    inlines = [
        BookInfoInline,
        HotelsCommentInline,
    ]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "address"],
            },
        ),
        (
            "Additional info",
            {
                "classes": ["collapse"],
                "fields": [("stars", "city", "phone"), "owners"],
            },
        ),
    ]


class HobbiesAdmin(admin.ModelAdmin):
    list_display = ["name", "experience"]
    search_fields = ["name", "experience"]
    list_filter = ["name"]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id_card_number", "serial", "persons"]


class BookOrderInfoAdmin(admin.ModelAdmin):
    list_display = ["detail", "time_order", "persons", "hotels"]


class HotelsCommentAdmin(admin.ModelAdmin):
    list_display = ["hotels", "persons", "comment"]




class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "sex"]
    search_fields = ["first_name", "last_name", "age", "sex"]
    list_filter = ["first_name", "last_name"]
    list_editable = ["age"]
    inlines = [
        HobbiesInline,
    ]


class PersonCommentAdmin(admin.ModelAdmin):
    list_display = ["person_rating", "hotels", "persons"]

admin.site.register(User, UserAdmin)
admin.site.register(PersonComment, PersonCommentAdmin)
admin.site.register(Persons, PersonsAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Hotels, HotelsAdmin)
admin.site.register(HotelsComment, HotelsCommentAdmin)
admin.site.register(BookOrderInfo, BookOrderInfoAdmin)
admin.site.register(Hobbies,HobbiesAdmin)
admin.site.register(HotelOwner, HotelOwnerAdmin)
