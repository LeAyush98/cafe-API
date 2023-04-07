from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def __init__(self, name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price) -> None:
        self.name = name
        self.map_url = map_url
        self.img_url = img_url
        self.location = location
        self.seats = seats
        self.has_sockets = has_sockets
        self.has_toilet = has_toilet
        self.has_wifi = has_wifi
        self.can_take_calls = can_take_calls
        self.coffee_price = coffee_price
        
    
    def get_dict(self) -> dict:
        data_dictionary = {}
        for column in self.__table__.columns:
            data_dictionary[column.name] = getattr(self, column.name) # go through this again

        return data_dictionary