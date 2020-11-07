# 1.파이썬 2.장고 3.외부패키지 4.어플리케이션
from django.db import models
from core import models as core_model
from users import models as users_model
from django_countries.fields import CountryField


class AbstractItem(core_model.TimeStampModel):

    """ abstract item """

    name = models.CharField(max_length=50)
    description = models.TextField(default="", blank=True)

    class Meta:
        abstract = True

    def __str__(self):

        return self.name


class RoomType(AbstractItem):
    """ ROOM TYPE model """

    class Meta:
        verbose_name = "Room Type"
        ordering = ["created"]


class Amenity(AbstractItem):

    """ Amenity model"""

    class Meta:

        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility model"""

    class Meta:

        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule model"""

    class Meta:

        verbose_name = "House Rule"


class Photo(AbstractItem):

    """ photo model"""

    caption = models.CharField(max_length=50)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_model.TimeStampModel):
    """ room model """

    name = models.CharField(max_length=40)
    descriptions = models.TextField()
    countries = CountryField()
    city = models.CharField(max_length=50)
    price = models.IntegerField()
    address = models.CharField(max_length=50)
    beds = models.IntegerField()
    baths = models.IntegerField()
    guest = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # foreign key인 host(user)가 room을 가르키니 namesehoon.room_set으로 접근할 수 있다.
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    # 방이 없어져도 룸타입 객체를 없애고 싶지는 않아
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    houserule = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name
