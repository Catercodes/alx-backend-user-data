#!/usr/bin/python3
"""the python shebang"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.errorhandler(401)
def request_unauthorized(error):
    """
     GET /api/v1/unauthorized
    return:
       - 401 error
    """
    return jsonify({"error": "Unauthorized"}, 401)


@app.errorhandler(404)
def not_found(error):
    """This is the default 404 error"""

    response = jsonify({"error": "Not Found"})
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
