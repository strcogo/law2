from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/aula")
@app.route("/aula/<name>")
@app.route("/aula/<name>/<curso>")
@app.route('/aula/<name>/<curso>/<int:ano>')
def aula(name = "juan", curso = "informatica", ano = 2):
    dados = {'name':name, 'curso':curso, 'ano':ano}
    return render_template("aula.html", dados_curso = dados)

if __name__ == '__main__':
    app.run()