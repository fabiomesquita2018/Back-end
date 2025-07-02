from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)


    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estacionamento.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco
    db.init_app(app)

    # Importa e registra o blueprint
    from .routes import main
    app.register_blueprint(main)
    
    CORS(app)
    

    # ⛑️ Adiciona cabeçalho de segurança após cada resposta
    @app.after_request
    def set_secure_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response

    # Cria as tabelas do banco de dados
    with app.app_context():
        db.create_all()

    return app
