from mealdelivery.celery import app
from menus.models import Menu, MenuLinkperEmployee
from employees.models import Employee
from .utils import send_message
import logging

@app.task(name="send_menu_via_slack")
def send_menu_via_slack(menu_id):    
    try:
        menu = Menu.objects.get(pk=menu_id)
        if menu.active:
            for employee in Employee.objects.all():
                menu_link, _ = MenuLinkperEmployee.objects.get_or_create(employee=employee, menu=menu)
                send_message(menu_link)
                logging.info(f'Successfully send message to {employee.name}')
        else:
            logging.info(f"Menu is not active ...")   
    except Menu.DoesNotExist:
        logging.info(f"Menu doesnt exist ...")