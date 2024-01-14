import db.models
import init_django_orm
import settings
from db.models import Car


def main():
    carr = Car.objects.create(
        brand="Skoda",
        horse_power=220,
        creation_date="2021-01-01",
    )
    print(carr)


if __name__ == "__main__":
    main()
