from flask import Flask

nome="Davi"
idade= 23
app=Flask(__name__)
@app.route("/login")
def login():
    return f'<h1> Bem-vindo{nome}, {idade} ao sistema </h1> '
if __name__=="__main__":
    app.run(debug=True)
