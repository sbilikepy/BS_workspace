import init_django_orm  # noqa: F401
from db.models import Place, Caffe
import datetime


def main():
    # def get_time(func):
    #     def wrapper():
    #         time_start = datetime.datetime.now()
    #         func()
    #         print(f"it takes: {datetime.datetime.now()-time_start}")
    #     return wrapper

    place = Place.objects.create(address="132. The Ramblas", post_index=198543)
    caffe1 = Caffe.objects.create(name="Best ever caffe3", place=place)

    # caffe2 = Caffe.objects.create( #UNIQUIE ERROR
    #     name = "Another caffe",
    #     place = place
    # )

    print(Caffe.objects.all())
    # print(caffe1.place == caffe2.place)

    # sppedtest
    # counter = 0
    # for i in range(2_000):
    #     Book.objects.create(
    #         title="Story about king Arthur "+str(counter),
    #         price=counter,
    #         format=novels
    #     )
    #     counter += 1


if __name__ == "__main__":
    Place.objects.all().delete()
    Caffe.objects.all().delete()
    main()
