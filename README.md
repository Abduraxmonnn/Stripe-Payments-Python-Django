# Stripe Python Library

[![pypi](https://img.shields.io/pypi/v/stripe.svg)](https://pypi.python.org/pypi/stripe)
[![Build Status](https://github.com/stripe/stripe-python/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/stripe/stripe-python/actions?query=branch%3Amaster)
[![Coverage Status](https://coveralls.io/repos/github/stripe/stripe-python/badge.svg?branch=master)](https://coveralls.io/github/stripe/stripe-python?branch=master)

## Documentation

See the [Python API docs](https://stripe.com/docs/api?lang=python).

See [Django docs](https://www.djangoproject.com/) covering how to use the library.

## About Project
This project created in [Python](https://www.python.org/) [Django](https://www.djangoproject.com/) and work with Stripe. 
When a get request is received on the backend, it creates the same product with a post request for the 
[Stripe](https://www.stripe.com) and returns the session id. In additional, customized Django admin panel for items. I also wrote a small instruction on cloning and running the project without Docker.

## Tech

* [Django](https://www.djangoproject.com/) - is a high-level `Python Web framework`
* [PostgreSQL](https://www.postgresql.org/) - open source object-relational database system

And many other libraries.

### Requirements
[Python](https://www.python.org) 3.8 or 3.6+

```shell
$ git clone https://github.com/Abduraxmonnn/stripe_billing.git
$ cd stripe_billing
```

***

## Setting project

## Usage

The library needs to be configured with your account's secret key which is
available in your [Stripe Dashboard](https://dashboard.stripe.com/). Set `stripe.api_key` to its value:
You should get your own `api_key` from [Dashboard](https://dashboard.stripe.com/) and set it to
* `STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLIC_KEY')`
* `STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')`

put own `api_ley` in `STRIPE_SECRET_KEY` in `stripe_billing/settings.py`

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
