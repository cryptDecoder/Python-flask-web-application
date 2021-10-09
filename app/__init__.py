from flask import Flask

app = Flask(__name__)

# import views
from app.views import views