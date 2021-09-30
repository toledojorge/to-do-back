from app.model.person import Person

class PersonService:

    def __init__(self, person_repository):
        self.person_repository = person_repository

    def get_all(self):
        return self.person_repository.get_all()

    def get(self, id: int):
        return self.person_repository.get(id)

    def insert(self, person: Person):
        return self.person_repository.insert(person)

    def update(self, person: Person, id: int):
        return self.person_repository.update(person,id)

    def delete(self, id: int):
        return self.person_repository.delete(id)