from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Dessert", price=120, inventory=50)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "Dessert : 120")