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


class TestProductUrls(TestCase):
    def setUp(self):
        Category.objects.create(
            id=1,
            name="jeans",
            slug="aa",
            created_at="2012-07-23",
            updated_at="2012-07-24",
        )
        Category.objects.create(
            id=2,
            name="shirt",
            slug="bb",
            created_at="2012-07-20",
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

    def test_product_detail(self):
        response = self.client.post(reverse("shop:product_detail", args=[1, "aa"]))
        self.assertEqual(response.status_code, 200)
