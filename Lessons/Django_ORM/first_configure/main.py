import init_django_orm  # noqa: F401
from db.models import Book, LiteraryFormat


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
    main()
