from app import ma

class CardSchema(ma.Schema):
    class Meta:
        fields = ('id','name','description','state')