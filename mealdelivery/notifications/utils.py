import requests
import os
import logging

# curl -X POST -H 'Content-type: application/json' --data '{"text":"Hola {employee.name} {} "}' https://hooks.slack.com/services/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
# curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World! jluis avila"}' https://hooks.slack.com/services/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

def post_to_slack(message, SLACK_WEBHOOK_URL):
    data = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=data, verify=False)
    if not response.ok:
        logging.info(f"request to slack, was not possible ...")


def execute(
    employee,
    menu
):
    msg = f"Hola: {employee.name} \n"
    msg = msg + f"Selecciona tu menu : {employee.menu.link} \n"
    msg = msg + f"Fecha: {menu.created} \n"

    post_to_slack(msg, )
