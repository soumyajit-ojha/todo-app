# todo-app
A simple TODO application made with DRF.
# TODO API (Django REST Framework)

A simple TODO application API built with Django 5.2 and Django REST framework 3.16.

## Prerequisites

- Python 3.13.3  
- pip (comes with Python)  
- (Optional but recommended) virtualenv or [poetry](https://python-poetry.org)

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/soumyajit-ojha/todo-app.git
   cd todo-api

2. **Create & activate your virtual environment**
   ```python -m venv .venv
   ```
    # On Windows
    ```
    .venv\Scripts\activate
    ```
    # On macOS/Linux
    ```
    source .venv/bin/activate
    ```
3. **Install dependencies**
    ```
        pip install -r requirements.txt
    ```

4. **Apply migrations**
    ```
    python manage.py migrate
    ```
5. **Create a superuser (optional, for admin access)**
    ```
        python manage.py createsuperuser
    ```

## Running the Development Server
    ```python manage.py runserver
    ```

    Visit http://127.0.0.1:8000/api/todos/ to explore the browsable API.

