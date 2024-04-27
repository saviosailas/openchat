# openchat
Openchat Flask website http://openchat.pythonanywhere.com/


#### Create virtual environemnt (Optional)

`python -m venv .venv`

`source .venv/bin/activate`

#### Install dependencies

`python -m pip install -r requirements.py`

#### Setup database

`python -m flask create-database`

#### Run app

` python -m flask run`

 flask will auto run `wsgi.py` or `app.py`



#### Miragte database (Optional)

Initialize database/migration config

 `python -m flask db init`

Create migrate

`python -m flask db migrate -m \"Initail migrattion\"`

Upgrade database

`python -m flask db upgrade`

