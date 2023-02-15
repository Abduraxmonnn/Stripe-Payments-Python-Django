## About Project
This project created in [Python](https://www.python.org/) [Django](https://www.djangoproject.com/) and work with Stripe. 
When a get request is received on the backend, it creates the same product with a post request for the 
[Stripe](https://www.stripe.com) and returns the session id. In additional, customized Django admin panel for items. I also wrote a small instruction on cloning and running the project without Docker.

## Tech

* [Django](https://www.djangoproject.com/) - is a high-level `Python Web framework`
* [PostgreSQL](https://www.postgresql.org/) - open source object-relational database system

And many other libraries.

Dillinger requires [Python](https://www.python.org) v3.4+.

```shell
$ git clone https://github.com/Abduraxmonnn/stripe_billing.git
$ cd stripe_billing
```

***

## Setting project

* `Linux`
```shell
$ virtualenv -p /usr/bin/python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

* `Windows`
```shell
$ python -m venv ./venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

* `MacBook`
```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

***

## Development
### Run Project
```shell
$ python manage.py runserver
```
`Output`
```shell
System check identified no issues (0 silenced).
Month date, year - hh:mm:ss
Django version 3.2.15, using settings 'stripe_billing.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Open http://127.0.0.1:8000 in your browser for see result.
