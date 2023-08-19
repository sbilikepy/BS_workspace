import datetime

import init_django_orm  # noqa: F401
from db.models import Book, LiteraryFormat, Author
from services import book as book_service


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
    # books = ["book_1", "book_2", "book_3", "book_4"]
    # counter = 10
    # for i in books:
    #     Book.objects.get_or_create(
    #         title=i,
    #         price=counter,
    #         format=random.choice(LiteraryFormat.objects.all())
    #     )
    #     counter += 1

    biography = LiteraryFormat.objects.create(
        format="biography"
    )

    robert = Author.objects.create(
        first_name="Robert",
        last_name="Kiyosaki"
    )
    sharon = Author.objects.create(
        first_name="Sharon",
        last_name="Lechter"
    )
    robert.save()
    sharon.save()

    # r_d = Book.objects.create(
    #     title= "Rdpd",
    #     price=25.5,
    #     format=biography
    # )
    # r_d.authors.add(
    #     robert,sharon
    # )
    #####################################################
    mystery = LiteraryFormat(format="mystery")
    mystery.save()

    arthur = Author(first_name="Arthur", last_name="Conan Doyle")
    arthur.save()

    # sherlock_holmes_book = Book(
    #     title="Sherlock Holmes",
    #     price=22.5,
    #     format = mystery)
    # sherlock_holmes_book.save()
    # sherlock_holmes_book.authors.add(
    #     arthur
    # )
    # print(sherlock_holmes_book.authors.all())
    #######____REMOVE_DATA_WITH_RELATIONS__#################
    # book = Book.objects.create(
    #     title="Harry Potter and the Cursed Child",
    #     price=17.5,
    #     format_id=LiteraryFormat.objects.get(
    #         format="mystery"
    #     ).id
    # )
    # print(book.__str__())
    # book.authors.set(
    #     [Author.objects.get(
    #         first_name="William"
    #     ),
    #         Author.objects.get(
    #             first_name="James"
    #         ),
    #         Author.objects.get(
    #             first_name="Jane"
    #         )
    #     ]
    # )
    # print(book.delete()) # return deleted elements
    ##########___SERVICES____########################


if __name__ == '__main__':
    del_all()
    main()
    authors_id = [
        Author.objects.get(first_name="Robert").id,
        Author.objects.get(first_name="Sharon").id

    ]
    book_2 = book_service.create_book(
        title="RdPd",
        price=17.5,
        format_id=LiteraryFormat.objects.get(
            format="mystery"
        ).id
    )
    book_2.authors.set(authors_id)
    get_mys_id = LiteraryFormat.objects.get(format="mystery").id
    print(get_mys_id)
    print(book_service.get_books(
        format_id=get_mys_id,
        authors_ids=[1255, 12312]  # 911 <QuerySet [RdPd 17.50 mystery]>
    ))
    #####19.08#####
    #### Django ORM / Queries in Details #####
    drama = LiteraryFormat.objects.get(format="Drama")
    some_book = Book.objects.create(price="14.23", format=drama)
    # ANNOTATE (for whole table)
    # print(Book.objects.all().aggregate(Avg("price")))
    # for i in Book.objects.aggregate(
    #         Avg("price"),
    #         Max("price"),
    #         Min("price"),
    #         Sum("price"),
    #         Count("price")
    # ).items():
    #     print(i)

    # ANNOTATE (for every raw)
    # print(Book.objects.annotate(
    #     num_authors=Count("authors")
    # ).values("title", "num_authors"))
    #
    # print(Author.objects.annotate(
    #     num_books=Count("by_author"))
    #        .values("first_name", "last_name", "num_books"))

    # print(LiteraryFormat.objects.annotate(
    #     num_books=Count("by_format")
    # ).values())

    # print(LiteraryFormat.objects.annotate(
    #     avg_price=Avg("by_format__price")
    # ).values())
    # Author.objects.create(
    #     first_name="Arthur",last_name="Bobo"
    # )
    # print(Author.objects.
    #       filter(
    #     last_name__contains="o"
    # ).values(
    #     "first_name","last_name"
    # ).
    #       annotate(
    #     Count(
    #         "first_name")))
    #
    #
    # print(
    #     Author.objects.
    #     filter(
    #         last_name__contains="o"
    #     ).values(
    #         "first_name", "last_name"
    #     ).
    #     annotate(Count(
    #         "first_name")).filter(
    #         first_name__count__gte=1
    #     )
    # )
    ################ N+1 problem ####################
    ### SELECT RELATED
    # print(Book.objects.all()) # -> several req if for example
    # __str__ contains self.format.name etc.
    # better use .select_related()
    # print(Book.objects.all().select_related("format")) # 1 req

    ##### PREFETCH_RELATED
    # for book in Book.objects.all().prefetch_related(): # 2 request, not 5 :)
    #     authors = [author.first_name for author in book.authors.all()]
    #     print("BOOK->", book.title, authors)
    #
    # for lit_format in LiteraryFormat.objects.all(): # 3 requests
    #     books = [book.title for book in lit_format.by_format.all()]
    #     print("LF->", lit_format.format, books)

    for lit_format in LiteraryFormat.objects.all(

    ).prefetch_related("by_format"):  # 2 req, not n+1
        books = [book.title for book in lit_format.by_format.all()]
        print("LF->", lit_format.format, books)



