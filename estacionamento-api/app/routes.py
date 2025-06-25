from flask import Blueprint, request, jsonify
from .models import Carro
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/carros', methods=['POST'])
def adicionar_carro():
    data = request.get_json()
    try:
        carro = Carro(
            marca=data['marca'],
            placa=data['placa'],
            entrada=datetime.strptime(data['entrada'], "%Y-%m-%d %H:%M:%S"),
            saida=datetime.strptime(data['saida'], "%Y-%m-%d %H:%M:%S")
        )
        db.session.add(carro)
        db.session.commit()
        return jsonify({'mensagem': 'Carro adicionado com sucesso'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

@main.route('/carros', methods=['GET'])
def listar_carros():
    carros = Carro.query.all()
    return jsonify([c.to_dict() for c in carros])

@main.route('/carros/<int:id>', methods=['DELETE'])
def deletar_carro(id):
    carro = Carro.query.get(id)
    if carro:
        db.session.delete(carro)
        db.session.commit()
        return jsonify({'mensagem': 'Carro removido'})
    return jsonify({'erro': 'Carro não encontrado'}), 404

@main.route('/carros/filtrar', methods=['GET'])
def filtrar_carros():
    query = Carro.query
    marca = request.args.get('marca')
    placa = request.args.get('placa')
    entrada_de = request.args.get('entrada_de')
    entrada_ate = request.args.get('entrada_ate')

    if marca:
        query = query.filter(Carro.marca.ilike(f"%{marca}%"))
    if placa:
        query = query.filter(Carro.placa.ilike(f"%{placa}%"))
    if entrada_de:
        query = query.filter(Carro.entrada >= datetime.strptime(entrada_de, "%Y-%m-%d"))
    if entrada_ate:
        query = query.filter(Carro.entrada <= datetime.strptime(entrada_ate, "%Y-%m-%d"))

    return jsonify([c.to_dict() for c in query.all()])
