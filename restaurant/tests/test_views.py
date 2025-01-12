from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from restaurant.serializers import MenuSerializer
from restaurant.models import Menu


class MenuItemsViewTest(TestCase):
    def setup(self):
        self.item1 = Menu.objects.create(title="IceCream", price=80.05, inventory=80)
        self.item2 = Menu.objects.create(title="Pasta", price=35.05, inventory=38)
        self.item3 = Menu.objects.create(title="Beef Steak", price=100, inventory=120)

        self.client = APIClient()  # Initialize API client for sending requests

    def test_getall(self):
        """
        Retrieve all Menu objects and check if serialized data matches the response.
        """
        # Get all menu items
        response = self.client.get(reverse("menu-items"))

        # Serialize the data
        menu_items = Menu.objects.all()
        serialized_data = MenuSerializer(menu_items, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serialized_data)
