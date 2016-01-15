from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

#models
from models import Registry

#controllers
from .controllers import Read

#DB
from contextlib import closing
from .config import DevelopmentConfig
from .database import db_session
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
from .database import init_db
init_db()

#REST
from flask_restful import Resource, Api
api = Api(app)

api.add_resource(Read, '/read')




if __name__ == '__main__':
	app.run()












'''
app.config.update(
	CELERY_BROKER_URL='redis://localhost:6379',
	CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)


@celery.task()
def add_together(a, b):
	return a + b
'''