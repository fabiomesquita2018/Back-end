from flask import Blueprint, request, jsonify
from .models import Carro
from . import db
from datetime import datetime


main = Blueprint('main', __name__)
# Rotas do aplicativo MVP para gerenciar carros em um estacionamento
# Rota que define a inserção de um carro no estacionamento
@main.route('/carros', methods=['POST'])
def adicionar_carro():
    """
    Adiciona um carro ao estacionamento.
    ---
    tags:
      - Carros
    parameters:
      - in: body
        name: body
        required: true
        schema:
          properties:
            marca:
              type: string
            placa:
              type: string
            entrada:
              type: string
              example: "2025-07-02 10:00:00"
            saida:
              type: string
              example: "2025-07-02 18:00:00"
    responses:
      201:
        description: Carro adicionado com sucesso
      400:
        description: Erro ao adicionar carro
    """
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
    """
    Lista todos os carros cadastrados.
    ---
    tags:
      - Carros
    responses:
      200:
        description: Lista de carros
    """
    carros = Carro.query.all()
    return jsonify([c.to_dict() for c in carros])

@main.route('/carros/<int:id>', methods=['DELETE'])
def deletar_carro(id):
    """
    Remove um carro pelo ID.
    ---
    tags:
      - Carros
    parameters:
      - in: path
        name: id
        required: true
        type: integer
    responses:
      200:
        description: Carro removido
      404:
        description: Carro não encontrado
    """
    carro = Carro.query.get(id)
    if carro:
        db.session.delete(carro)
        db.session.commit()
        return jsonify({'mensagem': 'Carro removido'})
    return jsonify({'erro': 'Carro não encontrado'}), 404

@main.route('/carros/filtrar', methods=['GET'])
def filtrar_carros():
    """
    Filtra carros por marca, placa e datas de entrada.
    ---
    tags:
      - Carros
    parameters:
      - in: query
        name: marca
        type: string
      - in: query
        name: placa
        type: string
      - in: query
        name: entrada_de
        type: string
        example: "2025-07-01"
      - in: query
        name: entrada_ate
        type: string
        example: "2025-07-02"
    responses:
      200:
        description: Lista de carros filtrados
    """
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


