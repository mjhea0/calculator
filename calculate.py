from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def calculate():
    if request.method == "POST":
        num1 = int(request.form['x'])
        print num1
        num2 = int(request.form['y'])
        operator = request.form['operator']
        if operator == '0':
           result = (num1 + num2)
        elif operator == '1':
          result = (num1 - num2)

        elif operator == '2':
           result = (num1 * num2)

        elif operator == '3':
           result = (num1 / num2)

        return render_template("index.html", result=result)        

    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)