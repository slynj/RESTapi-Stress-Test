from flask import *

app = Flask(__name__)

numbers = [
    {
        'name': u'Lyn',
        'number': 100
    },
    {
        'name': u'Bella',
        'number': 200
    }
]


# GET method - get everything
@app.route('/sum/getNumber', methods=['GET'])
def getNumbers():
    return jsonify({'numbers': numbers})


# GET method - get 1 number
@app.route('/sum/getNumber/<string:name>', methods=['GET'])
def getNumber(name):
    number = [number for number in numbers if number['name'] == name]
    if len(number) == 0:
        abort(404)
    return jsonify({'number': number[0]})


# GET method - get the sum of everything
@app.route('/sum/getSum', methods=['GET'])
def getSum():
    numbersSum = 0
    for number in numbers:
        numbersSum += number['number']
    return str(numbersSum)


# POST method - add a number
@app.route('/sum/postNumber', methods=['POST'])
def createNumber():
    # Adding data only if marked as JSON and has a number item
    if not request.json or not 'number' in request.json:
        abort(400)
    number ={
        'name': request.json['name'],
        'number': request.json['number']
    }
    numbers.append(number)
    return jsonify({'number': number}), 201


# With variable inputs
@app.route('/sum/<int:num1>/<int:num2>')
def returnSum(num1, num2):
    return str(num1 + num2)


# Pass the required route
@app.route("/hello")
def hello():
    return "Hello World"


@app.route('/')
def index():
    return "Home"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '404 Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
