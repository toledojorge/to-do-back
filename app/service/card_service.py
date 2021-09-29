from model.card import Card

class CardService:

    def __init__(self, card_repository):
        self.card_repository = card_repository

    def getAll(self):
        return self.card_repository.getAll()

    def get(self, id: int):
        return self.card_repository.get(id)

    def insert(self, card: Card):
        card.state = False
        return self.card_repository.insert(card)

    def update(self, card: Card, id: int):
        return self.card_repository.update(card,id)

    def delete(self, id: int):
        return self.card_repository.delete(id)