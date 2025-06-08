from flask import Flask
from flask_migrate import Migrate
from database import db
from __init__ import create_app

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()