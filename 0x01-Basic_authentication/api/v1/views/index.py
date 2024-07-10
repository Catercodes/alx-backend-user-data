from flask import Blueprint, abort
from api.v1.views import app
app_result = Blueprint('app_views', __name__)


@app.route('/api/v1/unauthorized', methods=['GET'])
def get_unauthorized():
    abort(401)
