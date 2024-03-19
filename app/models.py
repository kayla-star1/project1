from . import db

class Property(db.Model):

     __tablename__ = 'properties'

     propertyId = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(180),nullable=False)
     location = db.Column(db.String(280),nullable=False)
     no_of_bedrooms = db.Column(db.Integer,nullable=False)
     no_of_bathrooms = db.Column(db.Integer,nullable=False)
     price = db.Column(db.Integer,nullable=False)
     property_type = db.Column(db.String(15))
     description = db.Column(db.String(800))
     photo= db.Column(db.String,nullable=False)


     def __init__(self,title, location,no_of_bathrooms,no_of_bedrooms, price,property_type,description,photo):
         self.title = title 
         self.location = location
         self.no_of_bathrooms = no_of_bathrooms
         self.no_of_bedrooms = no_of_bedrooms
         self.price = price  
         self.property_type = property_type
         self.photo= photo
         self.description = description