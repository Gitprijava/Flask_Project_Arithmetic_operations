from flask import Flask, request,render_template


app = Flask(__name__)
#route
@app.route("/")
def hello_world():
    return  render_template("index.html")


@app.route("/aboutus")
def aboutus():
    return "Welcome"

@app.route("/operation",methods = ['POST'])
def operation():
    if(request.method=='POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0
        if operation == "add":
          result = num1 + num2
        elif operation == "multiply":
          result = num1 * num2
        elif operation == "division":
          result = num1 / num2
        else:
          result = num1 - num2
        return render_template("result.html",result = result)
        #return f'The operation is {operation} and result is {result}'





if __name__ == '__main__' :
    app.run(host = "0.0.0.0", port = 5000) 


