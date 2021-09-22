from flask import Flask, jsonify
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

    def __repr__(self):
        return "<Title: {}>".format(self.title)
    
@app.route("/api/card", methods=["GET"])
def home():
    cards = Card.query.all()
    return jsonify(cards)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
