from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "9970626666560a32465d4ce10d28f3233365af833e15eed59884d9477862c379"

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

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/dados", methods=["POST"])
def dados():
    flash("dados enviados!!")
    dados = request.form
    return render_template("dados.html", dados=dados)

if __name__ == '__main__':
    app.run()