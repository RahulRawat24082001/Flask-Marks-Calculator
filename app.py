from flask import Flask,render_template, request

## create a simple Flask Application

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def welcome():
    return "This my Flask project"

@app.route("/success/<int:score>")
def success (score):
    return "The Person had passed and the scode is :" + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has failed and the score is :" + str(score)

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else :
        Maths = float(request.form['Maths'])
        English = float(request.form['English'])
        Physics = float(request.form['Physics'])
        Chemistry = float(request.form['Chemistry'])
        Biology = float(request.form['Biology'])
        Average_marks = (Maths+English+Physics+Chemistry+Biology)/5
        return render_template('form.html',score=Average_marks)

if __name__ == "__main__":
    app.run(debug=True)





