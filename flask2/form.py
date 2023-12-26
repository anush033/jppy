from wtforms import Form,Stringfield,EmailField,validators
class UserForm(Form):
    username=Stringfield('username',[validators.length(min=4,max=25)])
    email=EmailField('Email',[validators.Email()])