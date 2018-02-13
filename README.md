# To excute this project

Please run the folllowing commands

$git clone git@bitbucket.org:mohank525/feature.git

$cd feature/
$pip3 install -r requirments.txt

Please edit the config.py

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<username>:<passowrd>@<host>/<db name>' 

$mysql -u root -p
>Enter your password
>create database <db name>;


$python3
>>> from app import db
>>> from models import Features
>>> db.create_all()

The above command create the database Schema in Database

Now, Please run the this command

$python3 app.py 

And hit this url in Browser http://http://127.0.0.1:8000/