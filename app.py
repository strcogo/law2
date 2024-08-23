from flask import Flask, render_template, request, flash
from database import db
from flask_migrate import Migrate
from models import Carros

app = Flask(__name__)
app.config["SECRET_KEY"] = "9970626666560a32465d4ce10d28f3233365af833e15eed59884d9477862c379"

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/lalau_db" # minha database
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/aula")
@app.route("/aula/<name>")
@app.route("/aula/<name>/<curso>")
@app.route('/aula/<name>/<curso>/<int:ano>')
def aula(name = "Carlos", curso = "carli", ano = 2):
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

@app.route("/carros")
def carros():
    car = Carros.query.all
    return render_template("carros.html", dados=car)

@app.route("/carros/add")
def carros_add():
    pass

if __name__ == '__main__':
    app.run()