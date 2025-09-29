idade= 23


v1=3
v2=5
soma2=v1+v2
subtração2=v1-v2
divisão2=v1/v2
multiplicação2=v1*v2
app=Flask(__name__)
@app.route("/login")
def login():
    return f'<h1> Bem-vindo{nome}, {idade} ao sistema </h1> '
@app.route("/operacoes")
def titulo_soma():
    return f'<h1> Calculadora </h1> '

@app.route("/soma")
def soma():
    return f"O resultado é:{soma2}"
@app.route("/subtracao")
def subtracao():
    return f"O resultado é:{subtração2}"

@app.route("/divisão")
def divisão():
    return f"O resultado é:{divisão2}"

@app.route("/multiplicação")
def multiplicação():
    return f"O resultado é:{multiplicação2}"
if __name__=="__main__":
    app.run(debug=True)
