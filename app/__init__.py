from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

from contextlib import closing
from app.config import DevelopmentConfig
from app.database import db_session
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


from app.database import init_db
init_db()


from models import Registry

'''
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
'''

@app.route('/')
def base():
	return 'This page is empty'

@app.route('/readall')
def readAll():
	print Registry.query.all()

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
		db_session.add(entry)
		print "qua"
		db_session.commit()
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