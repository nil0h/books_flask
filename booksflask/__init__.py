from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@server/db'.format(
            app.config.get('USER'), app.config.get('SECRET')
            )
    db = SQLAlchemy(app)


    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255))
        author = db.Column(db.String(255))
        genre = db.Column(db.String(255))

    @app.route('/', methods=['GET', 'POST'])
    def main():
        if request.method == 'GET':
            return "Hello " + request.args.get('name', '')

    return app
