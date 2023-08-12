import init_django_orm  # noqa: F401
from db.models import Order, Product, OrderItem



def main():
    pass


if __name__ == "__main__":
    # main()
    # iphone = Product.objects.create(
    #     name = "Iphone",
    #     price = 20_000.00
    # )
    # ipad = Product.objects.create(
    #     name="Ipad",
    #     price=30_000.00
    # )
    # mac = Product.objects.create(
    #     name="Macbook",
    #     price=70_000.00
    # )
    #
    # order_1 = Order.objects.create()
    # OrderItem.objects.create(
    #     order= order_1,
    #     product= iphone,
    #
    # )
    # OrderItem.objects.create(
    #     order=order_1,
    #     product=ipad,
    #
    # )
    #
    # order_2 = Order.objects.create()
    # OrderItem.objects.create(
    #     order= order_2,
    #     product=mac,
    #     amount=10
    # )

    print(Order.objects.all())
    order1 = Order.objects.first()
    print(order1.products.all())