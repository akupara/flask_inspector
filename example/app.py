import sys
import os

path_name = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path_name)


from flask import Flask
from flask_inspector import Inspector

app = Flask(__name__)

Inspector(app, base_path=path_name, username='admin', password='123')

app.run(debug=True)
# view  http://127.0.0.1:5000/inspector/
