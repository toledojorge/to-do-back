from app import db
from app.model.person import Person

class PersonRepository:

    def get_all(self):
        persons = Person.query.all()
        return persons

    def get(self, id: int):
        person = Person.query.get(id)
        return person

    def insert(self, person: Person):
        try:
            db.session.add(person)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Failed to insert person {e}")
            return False

    def update(self, person: Person, id: int):
        try:
            old_person = Person.query.get(id)
            old_person.email = person.email
            old_person.first_name = person.first_name
            old_person.last_name = person.last_name
            db.session.commit()
            return True
        except Exception as e:
            print(f"Failed to update person: {e}")
            return False

    def delete(self, id: int):
        try:
            person = Person.query.get(id)
            db.session.delete(person)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Failed to delete person {e}")
            return False