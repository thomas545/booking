
# Booking 
### Documentation:

1. [Django](https://docs.djangoproject.com/en/2.0/releases/2.0/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)
3. [API Translation](https://pypi.org/project/googletrans/)


### Installation:

1. Install git on Linux:  
`sudo apt-get install -y git`
2. Clone or download this repo.
3. Install pip and vitualenv on Linux:  
`sudo apt-get install -y virtualenv`  
`sudo apt-get install -y python3-pip`
4. Create a virtual environment on Linux or Mac:  
`virtualenv -p python3 ~/.virtualenvs/booking`
5. Activate the virtual environment on Linux or Mac:  
`source ~/.virtualenvs/booking/bin/activate`
6. Install requirements in the virtualenv:  
`pip3 install -r requirements.txt`

##### Relational database dependencies (PostgreSQL):
1. Install components for Ubuntu:  
`sudo apt-get update`  
`sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib`
2. Switch to **postgres** (PostgreSQL administrative user):  
`sudo su postgres`
3. Log into a Postgres session:  
`psql`
4. Create database with name **booking**:  
`CREATE DATABASE booking;`
5. Create a database user which we will use to connect to the database:  
`CREATE USER booking_user WITH PASSWORD 'booking_pass';`
6. Modify a few of the connection parameters for the user we just created:  
`ALTER ROLE booking_user SET client_encoding TO 'utf8';`  
`ALTER ROLE booking_user SET default_transaction_isolation TO 'read committed';`  
`ALTER ROLE booking_user SET timezone TO 'UTC';` 
7. Give our database user access rights to the database we created:  
`GRANT ALL PRIVILEGES ON DATABASE booking TO booking_user;`
8. Exit the SQL prompt and the postgres user's shell session:  
`\q` then `exit`

9. Activate the virtual environment:  
`source ~/.virtualenvs/booking/bin/activate`
10. Make Django database migrations:
`python manage.py makemigrations`  
then: `python manage.py migrate`

##### Use admin interface:
1. Run the project locally:  
`python manage.py runserver`
2. Navigate to: `http://localhost:8000/admin/`
 
##### Steps for install Celery and work it.
1. pip install -r requirements.txt
2. sudo apt-get install -y erlang
3. sudo apt-get install rabbitmq-server
4. sudo systemctl enable rabbitmq-server
5. sudo systemctl start rabbitmq-server to check if rabbitmq is working run: systemctl status rabbitmq-server
6. run local server for backend
7. run this command in new terminal in project path with activating virtual env: celery -A booking worker -l info


### API Endpoints
##### Register
Method: `POST`  
Endpoint: `/registration/`  
Payload:  
`{  
    "username": "USERNAME",  
    "password1": "PASSWORD",  
    "password2": "PASSWORD",  
    "email": "OPTIONAL_EMAIL"  
}`
##### Login
Method: `POST`  
Endpoint: `/login/`  
Payload:  
`{  
    "username": "USERNAME",  
    "password": "PASSWORD"  
}`

##### Logout
Method: `POST`  
Endpoint: `/logout/`  
Headers: `Authorization: JWT YOUR_TOKEN_HERE`  


### Admin Credentials
### Username: `admin`  
### Password: `admin` 

## For Dump and Load data

##### you should creating a folder to do this operations

##### for dump data from database:

###### python manage.py dumpdata products --format json --indent 4 > products/fixures/products.json

##### For loading data into database:
###### python manage.py loaddata products/fixures/products.json

## dump and restoredatabase:
#### pg_dump dbname=booking -f /tmp/booking.psql
#### pg_restore -v --host=<host> --port=5432 --username=<username> --password --dbname=booking /tmp/booking.psql


