from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import json

project_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:Thispassword123*@localhost:3399/to_do'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    state = db.Column(db.Boolean(), nullable=False)
    
@app.route("/api/card", methods=["GET"])
def getAll():
    cards = Card.query.all()
    return jsonify(cards)


@app.route("/api/card", methods=["POST"])
def insert():
    try:
        body = request.get_json()
        card = Card(name=body['name'], 
            description=body['description'], 
            state=False)

        db.session.add(card)
        db.session.commit()
        return jsonify(True)
    except Exception as e:
        print("Failed to insert card")
        print(e)
        return jsonify(False)

@app.route("/api/card/<id>", methods=["PUT"])
def update(id):
    try:
        body = request.get_json()
        card = Card.query.get(id)
        card.name = body['name']
        card.description = body['description']
        card.state = body['state']
        db.session.commit()
        return jsonify(True)
    except Exception as e:
        print("Failed to update card")
        print(e)
        return jsonify(False)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
