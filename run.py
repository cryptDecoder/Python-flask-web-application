"""
@title: run.py
@description: This is an entry point of flask application.
"""
import config
from app import app

app.config.from_object(config.DevConfiguration)
if __name__ == '__main__':
    app.run()
