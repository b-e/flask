from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

#DB config
from .config import DevelopmentConfig
app.config['SQLALCHEMY_DATABASE_URI'] = DevelopmentConfig.SQLALCHEMY_DATABASE_URI


#REST
from flask_restful import Resource, Api
from .controllers import RegistryCtrl

api = Api(app)

api.add_resource(RegistryCtrl, '/registry')