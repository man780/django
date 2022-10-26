# Installation

### 1. Clone from GitHub repository
```cmd
git clone https://github.com/man780/django.git
```

### 2. Change directory to django folder
```cmd
cd django
```

### 3. Install virtual environment. Then activate it
```cmd
python3 -m venv venv
source venv/bin/activate
```

### 4. Install libs
```cmd
pip install -r requirements.txt
```

### 5. Run server
```cmd
python manage.py runserver
```

## Don't use migrate commands.
It is already `python manage.py makemigrations` and `python manage.py migrate` 

This project has `db.sqlite3` file instead DB. There some data for using this project

Go to [main](https://github.com/man780/django)
