from flask import Flask, render_template, request, jsonify, make_response
from flask.ext import restful
from flask.ext.restful import reqparse

app = Flask(__name__)
api = restful.Api(app)

numbers = []

def solve(num1, num2):
    if request.form.get('add'):
        result = (num1 + num2)
    elif request.form.get('subtract'):
        result = (num1 - num2)
    elif request.form.get('multiply'):
        result = (num1 * num2)
    elif request.form.get('divide'):
        if num2 == 0:
            error = "Cannot divide by zero"
            return error
        else:
            result = (num1 / num2)
    elif request.form.get('equal'):
        error = "Please choose an operator"
        return error
    return result

class Numbers(restful.Resource):
    def get(self):
        return numbers

class Calculate(restful.Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200, headers) 
    
    def post(self):
        error = []
        result = []
        if request.method == "POST":
            num1 = int(request.form['x'])
            num2 = int(request.form['y'])
            global numbers
            numbers.append(num1) 
            numbers.append(num2)
            print numbers
            result = solve(num1, num2)
            print result
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('index.html', result=result, numbers=numbers, error=error),200, headers) 

        else:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('index.html', error=error),200, headers) 


api.add_resource(Calculate, '/', endpoint="index")
api.add_resource(Numbers, '/numbers', endpoint="numbers")


if __name__ == '__main__':
    app.run(debug=True)