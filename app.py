from flask import *
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

@app.route("/carros")
def carros():
    car = Carros.query.all()
    return render_template("carros.html", dados=car)

@app.route("/carros/add")
def carros_add():
    return render_template("carros_add.html")

@app.route("/carros/save", methods=["POST"])
def save():
    marca = request.form.get("marca")
    modelo = request.form.get("modelo")
    ano = request.form.get("ano")
    if marca and modelo and ano:
        carros = Carros(marca, modelo, ano)
        db.session.add(carros)
        db.session.commit()
        flash("Carro cadastrado")
        return redirect('/carros')
    else:
        flash("Preencha todos os campos")
        return redirect('/carros/add')
    
@app.route("/carros/remove/<int:id>")
def carros_remove(id):
    carros = Carros.query.get(id)
    if carros:
        db.session.delete(carros)
        db.session.commit()
        flash("Carro removido!!")
        return redirect("/carros")
    else:
        flash("Caminho Incorreto!!")
        return redirect("/carros")

@app.route("/carros/edit/<int:id>")
def carros_edit(id):
    try:
        carros = Carros.query.get(id)
        return render_template("carros_edit.html", dados=carros)
    except:
        flash("Carro Inválido")
        return redirect("/carros")
    
@app.route("/carros/editsave", methods=["POST"])
def carros_edit_save():
    id = request.form.get("id")
    marca = request.form.get("marca")
    modelo = request.form.get("modelo")
    ano = request.form.get("ano")

    if id and marca and modelo and ano:
        carro = Carros.query.get(id)
        carro.marca = marca
        carro.modelo = modelo
        carro.ano = ano
        db.session.commit()
        flash("Dados alterados com sucesso!!")
        return redirect("/carros")
    else:
        flash("Preencha todas as informações")
        return redirect("/carros/edit")

if __name__ == '__main__':
    app.run()