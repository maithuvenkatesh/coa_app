#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 5/27/2015
@author: iitoku2

Reads beach.config.py and
loads config into dashboard object depends on web server
'''

from flask import Flask
import os

from beach.config import Config


application = Flask(__name__)
application.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
application.config.from_object(Config)


from beach.views.contribution import cont
from beach.views.impact import imp

application.register_blueprint(cont, url_prefix='/contribution')
application.register_blueprint(imp, url_prefix='/impact')