from django.test import testcases, client, TestCase
from django.urls import resolve, reverse
from cart.views import cart_add, cart_remove, cart_detail
from orders.views import order_create
from orders.models import Order, OrderItem
from shop.models import Product, Category
from shop.views import product_list, product_detail
from cart.cart import Cart
from django.contrib.auth.models import User
import datetime


class TestCartUrls(TestCase):
    def setUp(self):
        Category.objects.create(
            id=1,
            name="jeans",
            slug="aa",
            created_at="2012-07-23",
            updated_at="2012-07-24",  # ,
        )
        Category.objects.create(
            id=2,
            name="shirt",
            slug="bb",
            created_at="2012-07-20",
            updated_at="2012-07-24",  # ,
        )
        Product.objects.create(
            id=1,
            name="shoes",
            slug="aa",
            category_id=1,
            description="Red color",
            price=1000,
            available=1,
            stock=10,
            created_at="2012-07-23",
            updated_at="2012-07-24",
        )
        Product.objects.create(
            id=2,
            name="cloth",
            slug="bb",
            category_id=2,
            description="Red color",
            price=12000,
            available=1,
            stock=5,
            created_at="2012-07-23",
            updated_at="2012-07-24",
        )
        Product.objects.create(
            id=3,
            name="watch",
            slug="aa",
            category_id=2,
            description="Red color",
            price=123000,
            available=1,
            stock=10,
            created_at="2012-07-23",
            updated_at="2012-07-24",
        )

    def test_cart_add_urls(self):
        response = self.client.post(reverse("cart:cart_add", args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_cart_details_urls(self):
        response = self.client.post(reverse("cart:cart_detail"))
        self.assertEqual(response.status_code, 200)


class TestOrderUrls(TestCase):
    def setUp(self):
        Category.objects.create(
            id=1,
            name="jeans",
            slug="aa",
            created_at="2012-07-23",
            updated_at="2012-07-24",  # ,
        )
        Product.objects.create(
            id=1,
            name="shoes",
            slug="aa",
            category_id=1,
            description="Red color",
            price=1000,
            available=1,
            stock=10,
            created_at="2012-07-23",
            updated_at="2012-07-24"  # ,
            # image="https://image.shutterstock.com/image-illustration/illustration-international-passengers-infrared-thermal-260nw-1640970700.jpg",
        )

    def test_order_create_urls(self):
        tdata = {
            "first_name": "abc",
            "last_name": "xyz",
            "email": "abc@hacker.com",
            "city": "tvw",
            "street": "tvw",
            "house_number": 1,
            "apartment_number": 1,
            "postal_code": 213456,
        }
        response = self.client.post(reverse("orders:order_create"), data=tdata)
        self.assertEqual(response.status_code, 400)


class TestOrderUrls1(TestCase):
    def setUp(self):
        Category.objects.create(
            id=1,
            name="jeans",
            slug="aa",
            created_at="2012-07-23",
            updated_at="2012-07-24",
        )
        Product.objects.create(
            id=1,
            name="shoes",
            slug="aa",
            category_id=1,
            description="Red color",
            price=1000,
            available=1,
            stock=10,
            created_at="2012-07-23",
            updated_at="2012-07-24",
        )
        Order.objects.create(
            id=1,
            first_name="rahul",
            last_name="kumar",
            email="rahul@gmail.com",
            city="bangalore",
            street="20",
            house_number="30",
            apartment_number="200",
            postal_code="565454",
            created="2012-01-03",
            updated="2013-02-03",
            paid=1,
        )
        OrderItem.objects.create(id=1, price=1000, quantity=1, order_id=1, product_id=1)

    def test_order_create_urls(self):
        response = self.client.post(reverse("orders:order_create"))
        self.assertEqual(response.status_code, 200)
