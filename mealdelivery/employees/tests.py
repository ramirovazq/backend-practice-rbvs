from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .models import Employee


class EmployeeTestCase(TestCase):
    def setUp(self) -> None:
        #  Create staff user
        self.user = User.objects.create_user(
            username="staff", email="staff@example.com", password="secret"
        )

        self.employee1 = Employee.objects.create(
            name="Felipe Gómez", slack_webhook_url="http://www.mealdelivery.test/felipe"
        )
        self.employee2 = Employee.objects.create(
            name="Maria Pérez", slack_webhook_url="http://www.mealdelivery.test/maria"
        )

        # Init Client
        self.client = Client()
        self.client.force_login(self.user)

    def test_list_employees_success(self):
        response = self.client.get(reverse("employees-index"))
        number_employees = len(response.context["employees"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(number_employees, 2)

    def test_employee_detail_success(self):
        included_str = f"<h1># {self.employee2.id}</h1>".encode("utf-8")
        response = self.client.get(
            reverse("employee-detail", kwargs={"pk": self.employee2.id})
        )
        response_employee = response.context["employee"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_employee.id, self.employee2.id)
        self.assertTrue(included_str in response.content)

    def test_create_employee_success(self):
        response = self.client.post(
            reverse("employee-create"),
            {
                "name": "Fernando",
                "slack_webhook_url": "http://www.testmeal.com/webhook",
            },
            follow=True,
        )
        number_employees = Employee.objects.all().count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(number_employees, 3)

    def test_edit_employee_success(self):

        response = self.client.post(
            reverse("employee-update", kwargs={"pk": self.employee2.id}),
            {
                "name": "Armando Gomez",
                "slack_webhook_url": self.employee2.slack_webhook_url,
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

        included_str = f"<h2>Name: Armando Gomez</h2>".encode("utf-8")
        response = self.client.get(
            reverse("employee-detail", kwargs={"pk": self.employee2.id})
        )
        self.assertTrue(included_str in response.content)
