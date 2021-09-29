from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:Thispassword123*@localhost:3399/to_do'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=5000, debug=True)