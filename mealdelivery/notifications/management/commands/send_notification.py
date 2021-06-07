from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites.models import Site
from menus.models import Menu, MenuLinkperEmployee
from employees.models import Employee
from notifications.utils import send_message

class Command(BaseCommand):
    help = 'Send notifications for specific menu_id'

    def add_arguments(self, parser):
        parser.add_argument('menus_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for menu_id in options['menus_ids']:
            try:
                menu = Menu.objects.get(pk=menu_id)
            except Menu.DoesNotExist:
                raise CommandError('Menu "%s" does not exist' % menu_id)

            if not menu.active:
                raise CommandError('Menu "%s" is not active' % menu_id)

            for employee in Employee.objects.all():
                menu_link, _ = MenuLinkperEmployee.objects.get_or_create(employee=employee, menu=menu)
                send_message(menu_link)
                self.stdout.write(self.style.SUCCESS('Successfully send message to "%s"' % employee.name))