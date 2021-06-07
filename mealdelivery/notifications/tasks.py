from mealdelivery.celery import app

@app.task(name="add")
def add(x, y):
    z = x + y
    print(z)