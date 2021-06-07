from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.urls.conf import include
from menus.models import Menu, MenuLinkperEmployee
from options.models import Option
from employees.models import Employee

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


class MenuLinkperEmployeeTest(TestCase):

    def setUp(self) -> None:
        # Create staff user 
        self.user = User.objects.create_user(
            username='staff', email='staff@example.com', password='secret')

        # Create menu
        self.menu = Menu.objects.create()
        self.option1 = Option.objects.create(name="Hamburguesa", menu=self.menu)
        self.option2 = Option.objects.create(name="Pizza", menu=self.menu)
        self.option3 = Option.objects.create(name="Ensalada", menu=self.menu)

        # Create menu
        self.employee1 = Employee.objects.create(name="Fernando", slack_webhook_url="http://hola.com/uuid1")
        self.employee2 = Employee.objects.create(name="Maria", slack_webhook_url="http://hola.com/uuid2")

        # Init Client
        self.client = Client()
        self.client.force_login(self.user)

    def test_menu_link_detail_success(self):
        included_str = f"<h1>Hello Fernando</h1>".encode("utf-8")
        included_str1 = f"Hamburguesa".encode("utf-8")

        menu_link = MenuLinkperEmployee(menu=self.menu, employee=self.employee1)
        menu_link.save()

        response = self.client.get(reverse('menu-link', kwargs={'uuid': menu_link.url_uuid}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(included_str in response.content)
        self.assertTrue(included_str1 in response.content)

    def test_employee_select_option(self):
        menu_link = MenuLinkperEmployee(menu=self.menu, employee=self.employee1)
        menu_link.save()

        response = self.client.get(reverse('menu-select-option', kwargs={'uuid': menu_link.url_uuid, 'option_id':self.option2.id}), follow=True)
        print(response.status_code)
        print("ping !")
        print(response.content)