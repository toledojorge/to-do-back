from app import ma

class PersonSchema(ma.Schema):
    class Meta:
        fields = ('id','email','first_name','last_name')