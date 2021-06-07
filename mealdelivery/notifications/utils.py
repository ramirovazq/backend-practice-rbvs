from django.contrib.sites.models import Site
import requests
import os
import logging

# curl -X POST -H 'Content-type: application/json' --data '{"text":"Hola {employee.name} {} "}' https://hooks.slack.com/services/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
# curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World! jluis avila"}' https://hooks.slack.com/services/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
# curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World! jluis avila"}' https://hooks.slack.com/services/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

def post_to_slack(message, SLACK_WEBHOOK_URL):
    data = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=data, verify=False)
    if not response.ok:
        logging.info(f"request to slack, was not possible ...")


def send_message(
    menu_link
):
    site = Site.objects.get_current()

    msg = f"Hi: {menu_link.employee.name} \n"
    msg = msg + f"Select your menu : http://{site.domain}/menus/{menu_link.url_uuid}/ \n"
    msg = msg + f"Fecha: {menu_link.menu.date_menu} \n"

    post_to_slack(msg, menu_link.employee.slack_webhook_url)
