from flask import Flask,render_template


app=Flask(__name__)
@app.route("/port")
def portifolio():
    return f'<h1> Bem-vindo </h1> '
@app.route('/home')
def correio():
    return render_template("port.html")


if __name__=="__main__":
    app.run(debug=True)
