"""
@tittle: views
@description: this is a base views of application
"""

# standard modules import
from app import app
from flask.views import MethodView
from flask import make_response, jsonify, request, redirect, url_for

# relative modules import
from app.utils import logger

log = logger.logger()

""" Creating example dictionary """

mobile = {
    "Samsung": {
        "description": "Android OS based mobile",
        "price": 122202
    },
    "iOS": {
        "description": "apple based iOS",
        "price": 45678
    }
}


class BaseViews(MethodView):
    """
    BaseViews class for all the base page route of the application.
    """

    def get(self):
        """ return the all data from mobile"""
        return make_response(jsonify(mobile), 200)

    def delete(self):
        """delele all details for mobile dict"""
        mobile.clear()
        log.info(mobile)
        return make_response(jsonify({}), 200)


app.add_url_rule("/api/base/", view_func=BaseViews.as_view("base_api"))
