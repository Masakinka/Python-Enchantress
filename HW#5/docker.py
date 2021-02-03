from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hi!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


tests = [
    {
        'id': 1,
        'title': u'Product',
        'description': u'DAC, ODAC, dbForge, ODBC, dotConnect',
        'done': False
    },
    {
        'id': 2,
        'title': u'Version',
        'description': u'Enterprise, Professional, Standard, Express',
        'done': False
    }
]


@app.route('/todo/api/v1.0/like_a_DB/<int:tests_id>', methods=['GET'])
def get_task(tests_id):
    test = filter(lambda t: t['id'] == tests_id, tests)
    if len(test) == 0:
        abort(404)
    return jsonify({'test': test[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
