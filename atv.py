from flask import Flask , jsonify
 
 app = Flask(__name__)
 @app.route ('/')
 def home():
    return  "<h1> Servidor Online!</h1 ><p> Bem-vindo ao Backend.</p>"
    @app.route('/saudacao/<nome>')
def saudacao(nome):
    return f"Ola, {nome}! Voce acessou uma rota dinamica "
@app.route( '/produto')
def listar_produtos():
    itens = ['Teclado', 'Mouse', 'Monito', 'Cadeira gamer']
    html = "<h2> Lista de produtos</h2><ul>"
    for i in itens:
        html += f "<li>{i}>/li."
    html += "</ul>"
    return html

@app.route ( '/somar/< int:v1 /<int:v2>')
def somar( v1, v2):
    res = v1 + v2 
    return f" O resultado da soma e:{res}"

@app.route ('/api status')
def status_api():
    dados = {
        "servidor": "HSC Core",
        "status": "operacional",
        "temperatura_cpu": 45.8,
        "usuarios_online": 12
        }
    return  jsonify(dados)

if --name-- '--main--':
    app.run(debug=True)