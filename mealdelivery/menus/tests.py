from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.urls.conf import include
from menus.models import Menu

class MenuTestCase(TestCase):

    def setUp(self) -> None:
        # Create staff user 
        self.user = User.objects.create_user(
            username='staff', email='staff@example.com', password='secret')

        # Create two menus
        self.menu1 = Menu.objects.create()
        self.menu2 = Menu.objects.create()

        # Init Client
        self.client = Client()
        self.client.force_login(self.user)

    def test_list_menu_success(self):
        response = self.client.get(reverse('menu-index'))
        number_menus = len(response.context['menus'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(number_menus, 2)

    def test_menu_detail_success(self):
        included_str = f"<h1># {self.menu2.id}</h1>".encode("utf-8")
        response = self.client.get(reverse('menu-detail', kwargs={'pk': self.menu2.id}))
        response_menu = response.context['menu']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_menu.id, self.menu2.id)
        self.assertTrue(included_str in response.content)


    def test_create_menu_success(self):
        response = self.client.get(reverse('menu-create'), follow=True)
        number_menus = Menu.objects.all().count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(number_menus, 3)


    def test_active_menu_success(self):
        self.assertTrue(self.menu1.active == False) # Initial condiction inactive
        included_str = f"Recordatory: active".encode("utf-8")
        response = self.client.post(reverse('menu-update', kwargs={'pk': self.menu1.id}), {'active': True}, follow=True)
        self.assertTrue(included_str in response.content)

