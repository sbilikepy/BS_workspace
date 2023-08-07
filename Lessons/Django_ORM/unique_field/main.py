import init_django_orm  # noqa: F401
from name_for_db.models import Company
def main():
    test_for_db = Company.objects.create(
        name="Sanya",
        age=30
    )
    test_for_db_2 = Company.objects.create(
        name="Asaj", age = 934
    )
if __name__ == '__main__':
    main()