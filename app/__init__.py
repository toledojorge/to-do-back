from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import api_bp

db = SQLAlchemy()

def run(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(api_bp)
    db.init_app(app)
    
    #app.run(host='0.0.0.0', port=5000, debug=True)
    return app