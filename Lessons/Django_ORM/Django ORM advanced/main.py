#from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.db import transaction
#from django.contrib.auth.models import User
import init_django_orm  # noqa: F401
from bus_station.models import Trip, Ticket, Bus, Order, User
import random


def main():
    pass


def clear_db():
    Trip.objects.all().delete()
    Ticket.objects.all().delete()
    Bus.objects.all().delete()
    Order.objects.all().delete()


def random_data():
    buses_list = ["Bohdan", "Mercedes", "BMW"]
    city_list = ["Kyiv", "Kharkiv", "Zaporizzhya", "Dnipro"]
    for bus in buses_list:
        Bus.objects.create(
            info=bus,
            num_seats=20
        )
    for city in city_list:
        Trip.objects.create(
            source=city,
            destination=random.choice(city_list),
            departure="2023-08-24",
            bus_id=Bus.objects.get(
                info=random.choice(buses_list)
            ).id)


def create_order(tickets: list[dict]):
    with transaction.atomic():

        new_order = Order.objects.create()
        for i in tickets:
            Ticket.objects.create(
                seat = i["seat"],
                trip_id = i["trip_id"],
                order_id = new_order.id
            )
        return new_order


if __name__ == '__main__':
    clear_db()
    # john = get_user_model().objects.create_user(
    #     username="Jo", email= "jo@gmail.com", password="jopassword"
    # )
    user = User.objects.get(username="Jo")

    user.set_password("sdfferferfsxxx")
    user.save()
    print(user.check_password("sdfferferfsxxx"))
    # random_data()
    #
    # create_order(
    #     tickets=[
    #         {
    #             "seat":10,
    #             "trip_id":Trip.objects.get(source="Kyiv").id
    #         },
    #         {
    #             "seat": 11,
    #             "trip_id": Trip.objects.get(source="Kyiv").id
    #         },
    #         {
    #             "seat": 12,
    #             "trip_id": Trip.objects.get(source="Kyiv").id
    #         }
    #     ]
    # )
