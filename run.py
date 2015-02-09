from flask import Flask, render_template, request, jsonify, make_response
from flask.ext import restful
from flask.ext.restful import reqparse

app = Flask(__name__)
api = restful.Api(app)

class Calculate(restful.Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200, headers) 
    
    def post(self):
        if request.method == "POST":
            
            num1 = int(request.form.get('num1'))
            num2 = int(request.form.get('num2'))
            operator = request.form.get(str('operator'))

            if operator == 'add':
                result = {'result': num1 + num2}
            if operator == 'subtract':
                result = {'result': num1 - num2}
            if operator == 'multiply':
                result = {'result': num1 * num2}
            if operator == "divide":
                if num2 == 0:
                    error = {'error': "Cannot divide by zero"}
                    return error
                else:
                    result = {'result': num1 / num2}

            print result
            return jsonify(result)
        else:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('index.html', error=error),200, headers) 


api.add_resource(Calculate, '/', endpoint="index")

if __name__ == '__main__':
    app.run(debug=True)