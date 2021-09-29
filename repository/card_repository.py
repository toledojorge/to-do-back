from app import db
from model.card import Card

class CardRepository:

    def getAll():
        cards = Card.query.all()
        return cards

    def get(id: int):
        card = Card.query.get(id)
        return card

    def insert(card: Card):
        try:
            card.state = False
            db.session.add(card)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Failed to insert card {e}")
            return False

    def update(card: Card, id: int):
        try:
            old_card = Card.query.get(id)
            old_card.name = card.name
            old_card.description = card.description
            old_card.state = card.state
            db.session.commit()
            return True
        except Exception as e:
            print(f"Failed to update card: {e}")
            return False

    def delete(id: int):
        try:
            card = Card.query.get(id)
            db.session.delete(card)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Failed to delete card {e}")
            return False