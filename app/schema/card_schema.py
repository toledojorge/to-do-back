from app import ma
from app.schema.person_schema import PersonSchema
class CardSchema(ma.Schema):    
    class Meta:
        fields = ('id','name','description','state','person')
        
    person = ma.Nested(PersonSchema)