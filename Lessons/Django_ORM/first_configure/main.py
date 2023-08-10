import datetime
import random
import init_django_orm  # noqa: F401
from db.models import Book, LiteraryFormat, Author


def get_time(func):
    def wrapper():
        time_start = datetime.datetime.now()
        func()
        print(f"it takes: {datetime.datetime.now() - time_start}")

    return wrapper


def del_all():
    try:
        Book.objects.all().delete()
        LiteraryFormat.objects.all().delete()
        Author.objects.all().delete()
    except Exception as e:
        print(e)


def main():
    authors = ["William Shakespeare", "Dante Alighieri", "Oscar Wilde",
               "Charles Dickens", "James Joyce", "Jane Austen"]
    for i in authors:
        Author.objects.get_or_create(
            first_name=i.split()[0],
            last_name=i.split()[1]
        )
    formats = ["Drama", "Fantasy", "Fiction", "Folclore"]
    counter = 10
    for i in formats:
        LiteraryFormat.objects.get_or_create(
            format=i
        )
    books = ["book_1", "book_2", "book_3", "book_4"]
    counter = 10
    for i in books:
        Book.objects.get_or_create(
            title=i,
            price=counter,
            format=random.choice(LiteraryFormat.objects.all())
        )
        counter += 1




if __name__ == '__main__':
    del_all()
    main()
