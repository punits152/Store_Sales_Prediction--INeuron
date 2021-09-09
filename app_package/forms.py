from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, IntegerField
from wtforms.validators import Email, EqualTo, Length

class PredictionForm(FlaskForm):
    price = DecimalField(label="Price of the Item : ")
    supermarket_type1 = IntegerField(label= "Is outlet in supermarket type1 : ")
    supermarket_type2 = IntegerField(label= "Is outlet in supermarket type2 : ")
    supermarket_type3 = IntegerField(label= "Is outlet in supermarket type3 : ")
    location_type_tier2 = IntegerField(label= "Is outlet in tier 2 city : ")
    fat_regular = IntegerField(label="Is the fat content regular : ")
    visibility = DecimalField(label="What is visibility percentage: ")
    submit = SubmitField(label="SUBMIT")






#(
 #   username = StringField(label="User Name : ", validators=[Length(min=2,max=30)])
  #  email_address = StringField(label="Email Address : ",validators=[Email()])
   # password1 = PasswordField(label="Password : ", validators=[Length(min=6)])
    #password2 = PasswordField(label="Confirm Password : ", validators=[EqualTo("password1")])
    #submit = SubmitField(label="Create Account"))
