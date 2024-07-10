#!/usr/bin/env python3
""" the shenbang"""
from flask import Blueprint, abort
from api.v1.views import app

app_result = Blueprint('app_views', __name__)


@app.route('/api/v1/unauthorized', methods=['GET'])
def get_unauthorized():
    """ testing the unauthorized route"""
    abort(401)
