
  <h2 align="center">Django Polls Application</h2>

  <p align="center" ><img src = "polls\static\image\image-re.png"></p>

This project is a simple Django application that implements a basic polls system, built as part of the Django tutorial.

## Getting Started

Follow the instructions below to set up and run the project locally.

### Installation Steps

1. **Install Django**
   ```bash
   pip install django
   ```

2. **Create a Django Project**
   ```bash
   django-admin startproject mysite djangotutorial
   cd ./djangotutorial
   ```

3. **Create the Polls App**
   ```bash
   python manage.py startapp polls
   ```

4. **Run the Development Server**
   Start the Django development server and verify the project:
   ```bash
   python manage.py runserver
   ```
   Navigate to `http://127.0.0.1:8000/polls` to see your project running!

### Useful Links

- [Django Documentation](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)
