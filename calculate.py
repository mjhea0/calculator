from flask import Flask, render_template, request, jsonify, make_response
from flask.ext import restful
from flask.ext.restful import reqparse

app = Flask(__name__)
api = restful.Api(app)

numbers = []

class Numbers(restful.Resource):
    def get(self):
        return numbers
    def put(self):
        numbers[value] = request.form[x]
        return {value: request.form[x]}

class Calculate(restful.Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200, headers) 
    
    def post(self):
        error = []
        result = []
        if request.method == "POST":
          numbers = [
              {
              'value': int(request.form['x']),
              },
              {
              'value': int(request.form['y'])
              }  
          ]
          for number in numbers:
            print number['value']
          print len(numbers)
          num1 = numbers[0]['value']
          num2 = numbers[1]['value']
          if request.form.get('add'):
              result = (num1 + num2)
          elif request.form.get('subtract'):
              result = (num1 - num2)
          elif request.form.get('multiply'):
              result = (num1 * num2)
          elif request.form.get('divide'):
              if num2 == 0:
                  error = "Cannot divide by zero"
              else:
                  result = (num1 / num2)
          headers = {'Content-Type': 'text/html'}
          return make_response(render_template('index.html', result=result, error=error),200, headers) 

        else:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('index.html', result=result, error=error),200, headers) 

api.add_resource(Calculate, '/', endpoint="index")
api.add_resource(Numbers, '/numbers', endpoint="numbers")


if __name__ == '__main__':
    app.run(debug=True)