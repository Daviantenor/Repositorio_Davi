from flask import Flask,render_template


app=Flask(__name__)
@app.route("/insta")
def instagram():
    return f'<h1> Bem-vindo ao instagram ,novo usuário </h1> '
@app.route('/rede')
def rede():
    return render_template("instagram.html")


if __name__=="__main__":
    app.run(debug=True)
