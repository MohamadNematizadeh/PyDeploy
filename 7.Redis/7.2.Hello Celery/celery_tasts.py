import os
from datetime import datetime
from time import sleep  # Import sleep for the dummy task
from celery import Celery  # Correct import statement


redis_url = "redis://localhost:6379"
app = Celery(__name__, broker=redis_url, backend=redis_url)

@app.task
def hello_world():
    return 'Hello, World!'

@app.task
def add(x, y):
    print("add function")
    return x + y

@app.task
def create_dummy_file():
    folder = "/tmp/celery"
    os.makedirs(folder, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")  # Correct format specifier for seconds
    with open(f"{folder}/task-{now}.txt", "w") as f:
        f.write("hello!")

@app.task        
def greet(name='Bob') -> str:
    sleep(5)
    return f'Hello {name}!'  # Ensure only one task with this name exists

@app.task
def write_to_file() -> str:
    with open('/tmp/celery/x.txt', 'w') as f:  # Use 'with' to manage file context
        f.write("Some data")  # Write some actual data to the file
    return "File written successfully"
