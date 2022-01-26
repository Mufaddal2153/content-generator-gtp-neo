import os
from flask import Flask


content = Flask(__name__)
content.config['SECRET_KEY'] = 'MyKey'

basedir = os.path.abspath(os.path.dirname(__file__))

