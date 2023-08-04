import init_django_orm  # noqa: F401
from db.models import LiteraryFromat


def main():
    # CRUD = object.+ create all update
    # print(LiteraryFromat.objects.all())  # objects Django builtin
    # new_format = LiteraryFromat.objects.create(format="test_genre")
    # poem_format = LiteraryFromat.objects.get(format="test_genre")
    # print(poem_format)
    # filtered_format = LiteraryFromat.objects.filter(
    #     format="poem"
    # ).update(format="poetry")  # show all
    # print(filtered_format)  # builder object returned, you can check query in debugger
    # update return amount of updated elements: int
    filtered_format = LiteraryFromat.objects.filter(
        format="drama"
    ).delete()  # no drama :)


if __name__ == '__main__':
    main()
