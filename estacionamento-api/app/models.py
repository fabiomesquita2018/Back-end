from . import db
from datetime import datetime

class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50), nullable=False)
    placa = db.Column(db.String(7), nullable=False, unique=True)
    entrada = db.Column(db.DateTime, nullable=False)
    saida = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'placa': self.placa,
            'entrada': self.entrada.strftime("%Y-%m-%d %H:%M:%S"),
            'saida': self.saida.strftime("%Y-%m-%d %H:%M:%S")
        }
