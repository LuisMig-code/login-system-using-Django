# Login System using Django
A simple login system using Django and PostgreSQL. Login , Register and Profile system including redirects system


## Functionalities
- Login and Register system
- If user logged , redirect for "profile" page
- Storing users in Postgresql
- The system prevents the creation of new users with usernames already created

## Tecnologias utilizadas
- Python 3
- DJango 5.2
- Postgres 17
- PSycopg2

## Prerequisites
- Python 3.x installed
- Postgres running locally or access to a remote cluster
- pip package manager

## Environment configuration
### 1) Clone the repository:
```bash
git clone https://github.com/LuisMig-code/login-system-using-Django.git
cd login-system-using-django
```

### 2) Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```

### 3) Install dependencies:
```bash
pip install -r requirements.txt
```

### 4) Configure the connection to Postgres:
- Create a .env file in the project root
- define the variables:
```
DB_NAME = YOUR_DB_NAME_POSTGRES
DB_USER = YOUR_DB_USER_POSTGRES
DB_PASSWORD = YOUR_DB_PASSWORD_POSTGRES
DB_HOST = YOUR_DB_HOST_POSTGRES (127.0.0.1 IF YOU'RE USING LOCALHOST)
DB_PORT = 5432
```

### 5) Configure the Secret Key :
- in .env file define the variable:
```
SECRET_KEY = YOUR_DJANGO_SECRET_KEY
```

## Executing the application:
``` bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000

## Usage:
### Go to the home page (/) to see the web interface
* If you're logged in, you'll see the profile page;
* if you're not logged in , the system will redirect you to login page;
* After registered , you'll be automatically redirected to login page;

## Project structure:
manage.py: Main django application
account/urls.py: Route system
account/views.py: Render website pages system
requirements.txt: Project dependencies
account/templates: HTML pages;
.env: File for environment variables (not versioned)

## Contribution:
Contributions are welcome! Feel free to open issues or pull requests.

