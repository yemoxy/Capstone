from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
       Menu.objects.create(title="Dessert", price=120, inventory=50)
       Menu.objects.create(title="Cake", price=100, inventory=5)
       

    def test_getall(self):
        dessert = Menu.objects.get(title='Dessert')
        cake = Menu.objects.get(title='Cake')
        self.assertEqual(str(cake), "Cake : 100.00")
        self.assertEqual(str(dessert), "Dessert : 120.00")