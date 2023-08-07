import init_django_orm  # noqa: F401
from db.models import Book, LiteraryFormat
import datetime
def get_time(func):
    def wrapper():
        time_start = datetime.datetime.now()
        func()
        print(f"it takes: {datetime.datetime.now()-time_start}")
    return wrapper

@get_time
def init():
    Book.objects.all().delete()
    LiteraryFormat.objects.all().delete()

    drama = LiteraryFormat.objects.create(
        format = "drama"
    )
    novels = LiteraryFormat.objects.create(
        format="novels"
    )
    Book.objects.create(
        title = "Hamlet",
        price = 10,
        format = drama
    )
    Book.objects.create(
        title = "Romeo",
        price = 10,
        format = drama
    )
    Book.objects.create(
        title = "HP",
        price = 10,
        format = novels
    )
    counter = 0
    #sppedtest
    # for i in range(2_000):
    #     Book.objects.create(
    #         title="Story about king Arthur "+str(counter),
    #         price=counter,
    #         format=novels
    #     )
    #     counter += 1
def main():
    # Book.objects.create(
    #     title = "",
    #     price = 10,
    #     format_id = 13
    # )

    print(Book.objects.get(title="Hamlet"))
    print(LiteraryFormat.objects.get(
        format="Drama"
    ).books.all() # One to many #related_name = "books"

    )


    Book.objects.filter(format__format="Drama").all() #format here -> LiterForm -> format.__name__
    print(str(Book.objects.filter(format__format="Drama").query)) #SCHECK SQL Q


if __name__ == '__main__':
    init()
    drama_format = LiteraryFormat.objects.get(
        format = "drama"
    )
    drama_format.delete()
