import init_django_orm  # noqa: F401
from db.models import LiteraryFormat, Author, Book


def main(*args, **kwargs):
    pass


if __name__ == "__main__":
    main()


# class Customer(models.Model):
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     phone_number = models.CharField(max_length=20)
#
#
# class LoyaltyProgram(models.Model):
#     name = models.CharField(max_length=64)
#     bonus_percentage = models.IntegerField()
#
#
# class LoyaltyProgramParticipant(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     loyalty_program = models.ForeignKey(LoyaltyProgram, on_delete=models.PROTECT)
#     last_activity = models.DateField(auto_now=True)
#     active_bonuses = models.IntegerField(default=0, null=True, blank=True)
#     sum_of_spent_money = models.IntegerField(default=0)
#
#
# from django.db.models import QuerySet
#
#
# def get_not_active_customers_names() -> QuerySet:
#     return LoyaltyProgramParticipant.objects.get(customer__first_name).filter(
#         last_activity="%y2021"
#     )
#
#
# def get_clients_with_i_and_o() -> QuerySet:
#     result = Customer.objects.filter(
#         Q(
#             first_name__startswith="I") | Q(
#             last_name__icontains="o"
#         ))
#     print(result)
#     return result
