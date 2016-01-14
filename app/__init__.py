import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
from app.config import DevelopmentConfig
from flask.ext.sqlalchemy import SQLAlchemy

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)

from models import Registry

@app.route('/')
def base():
	return 'This page is empty'

@app.route('/insertEntry')
def insertEntry():
	try:
		entry = Registry(
			token = 'bbbb',
			endpoint = 'ccccc',
			phoneNumber = 1981932,
			channel = 'bbbb',
			pid = 0
		)
		db.session.add(entry)
		print "qua"
		db.session.commit()
		return entry.id
	except Exception as e:
		print e

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