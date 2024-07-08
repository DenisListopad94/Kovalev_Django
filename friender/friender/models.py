from django.db import models
from .validators import users_age_validator
# Create your models here.

class User(models.Model):
    SEX_PERSON = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True, validators=[users_age_validator])
    sex = models.CharField(max_length=1, choices=SEX_PERSON, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    class Meta:
        indexes = [
            models.Index(fields=["first_name"], name="first_name_index"),
            models.Index(fields=["last_name"], name="last_name_index"),
            models.Index(fields=["age"], name="age_index"),
            models.Index(fields=["sex"], name="sex_index"),
        ]

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Persons(User):
    guest_rating = models.IntegerField(null=True)


class HotelOwner(User):
    owner_exp_status = models.IntegerField(null=True)


class Hotels(models.Model):
    name = models.CharField(max_length=40, null=True)
    stars = models.IntegerField(null=True)
    address = models.CharField(max_length=40, null=True)
    city = models.CharField(max_length=40, null=True)
    phone = models.CharField(max_length=40, null=True)
    photo = models.ImageField(null=True, upload_to="hotels_photo/")


    owners = models.ForeignKey(
        to="HotelOwner",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotels",
    )

    class Meta:
        indexes = [
            models.Index(fields=["name"], name="name_index"),
            models.Index(fields=["stars"], name="stars_index"),
            models.Index(fields=["city"], name="city_index"),
            models.Index(fields=["owners"], name="owners_index"),
        ]

    def __str__(self):
        return f" {self.name} "


class Comment(models.Model):
    comment = models.CharField(max_length=200, null=True)
    comment_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class Hobbies(models.Model):
    name = models.CharField(max_length=30, null=True)
    experience = models.IntegerField(null=True)
    owners = models.ManyToManyField(
        to="User",
        related_name="hobbies"
    )

    def __str__(self):
        return f" {self.name}"


class Profile(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to="profile_photo/")
    id_card_number = models.IntegerField(null=True)
    serial = models.FloatField(null=True)
    persons = models.OneToOneField(
        to="User",
        on_delete=models.CASCADE,
        null=True,
        related_name="profile"
    )


class BookOrderInfo(models.Model):
    detail = models.CharField(max_length=200, null=True)
    time_order = models.DateTimeField(auto_now_add=True)
    persons = models.ForeignKey(
        to="Persons",
        on_delete=models.SET_NULL,
        null=True,
        related_name='booking_info'
    )
    hotels = models.ForeignKey(
        to="Hotels",
        on_delete=models.SET_NULL,
        null=True,
        related_name='booking_info'
    )


class HotelsComment(Comment):
    hotel_rating = models.PositiveIntegerField(null=True)
    hotels = models.ForeignKey(
        to="Hotels",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotel_comments"
    )
    persons = models.ForeignKey(
        to="Persons",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotel_comments"
    )

    def __str__(self):
        return f" {self.comment}"


class PersonComment(Comment):
    person_rating = models.PositiveIntegerField(null=True)
    hotels = models.ForeignKey(
        to="Hotels",
        on_delete=models.SET_NULL,
        null=True,
        related_name="person_comments"
    )
    persons = models.ForeignKey(
        to="Persons",
        on_delete=models.SET_NULL,
        null=True,
        related_name="person_comments"
    )

    def __str__(self):
        return f" {self.comment}"
    
class Room(models.Model):
    hotel = models.ForeignKey(Hotels, related_name='rooms', on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

class Booking(models.Model):
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    customer_full_name = models.CharField(max_length=255)

class Queue(models.Model):
    item = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item