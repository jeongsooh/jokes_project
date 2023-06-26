from django.test import TestCase

from celery import Celery


app = Celery('tasks', broker='redis://localhost:6379')


@app.task
def add(x, y):
    print("Task is excuted")
    return x + y