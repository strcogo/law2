from database import db

class Carros(db.Model):
    
    __tablename__= "Carros"
    id_carros = db.Column(db.Integer, primary_key = True)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    ano = db.Column(db.SmallInteger)

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __repr__(self):
        return "<Marca {}>".format(self.marca)