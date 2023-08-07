import init_django_orm  # noqa: F401
from db.models import Company


def main():
    frist_company = Company.objects.create(
        company_name = "Microsoft",
        description="Bill Gates lose to Magnus Carlsen"
    )
    print("result: ",Company.objects.all)

if __name__ == '__main__':
    main()

# from django.db import models
#
#
# class Company(models.Model):
#     name = models.CharField(max_length=255),
#     description = models.TextField(blank=True)
#     weight = models.CharField(default="high")
#
#     # def __str__(self):
#     #     return f"{self.name}, {self.description}"
