from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def calculate():
  error = []
  result = []
  if request.method == "POST":
    num1 = int(request.form['x'])
    num2 = int(request.form['y'])
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
    return render_template("index.html", result=result, error=error)        

  else:
      return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)