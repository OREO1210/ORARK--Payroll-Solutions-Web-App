# ORAЯK
## Payroll Solutions

A simplified payroll and employee management system based on Django.



## Test Locally

### Clone the repo-
- `git clone https://github.com/da-r-k/orark`
### Installation-
#### Make sure to install django-
- `pip install django`
#### Windows-
- `cd orark`
- `py -m venv env`
- `env/Scripts/activate`
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`

#### Ubuntu-
- `cd orark`
- `sudo apt-get install python3-pip`
- `sudo pip3 install virtualenv`
- `virtualenv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`
