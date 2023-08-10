import init_django_orm  # noqa: F401
from db.models import LiteraryFormat,Author,Book
def main(*args, **kwargs):
    LiteraryFormat.objects.create(
        name = " :) "
    )

if __name__ == "__main__":
    main()
