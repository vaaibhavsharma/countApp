# count app

## Running Locally

- You should have Python 3.8 or higher installed.

### First Steps

```sh
git clone https://github.com/vaaibhavsharma/countApp.git
cd countApp
python3 -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```


### Django Configurations

```sh
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver 8080
```

Your local instance will now be up and running at http://127.0.0.1:8080/