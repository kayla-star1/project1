from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, DataRequired , Length
from flask_wtf.file import FileField, FileRequired, FileAllowed


class NewPropertyForm(FlaskForm):
     title = StringField('Property Title', validators=[InputRequired()])
     no_of_bedrooms = IntegerField('No. of Rooms', validators=[InputRequired()])
     no_of_bathrooms= IntegerField('No. of Bathrooms', validators=[InputRequired()])
     location= StringField('Location', validators=[InputRequired()])
     price=IntegerField('Price', validators=[InputRequired()])

     property_type=SelectField("Property Type", choices=[("House"),("Apartment")])
     description=TextAreaField("Description",validators=[DataRequired(),InputRequired(),Length(max=700)])

     pic=FileField("Photo", validators=[FileRequired(),FileAllowed(["jpg", "png","jpeg","Images only!"])])