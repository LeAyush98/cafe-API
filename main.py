from flask import Flask, jsonify, render_template, request, redirect, url_for
from db import db, Cafe
import random
from form import CafeForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

Bootstrap(app)

db.init_app(app)

@app.route("/")
def home():
   with app.app_context():
        db.create_all()   
   return render_template("index.html")
    

## HTTP GET - Read Record

@app.route("/random", methods = ["GET"])
def random_data():
    if request.method ==  "GET":
        cafe = random.choice(db.session.query(Cafe).all())
        return jsonify(cafe.get_dict())
    
@app.route("/all", methods = ["GET"])
def all():
    all_cafes = []
    if request.method == "GET":
        cafes = db.session.query(Cafe).all()
        for cafe in cafes:
            all_cafes.append(cafe.get_dict())
        return jsonify(all_cafes)
    
@app.route("/search", methods = ["GET"])    
def locate():
    if request.method == "GET":
        location = request.args.get("loc") # tap into the parameter value like this
        cafe = Cafe.query.filter_by(location=location).first()  
        if cafe:
            return jsonify(cafe.get_dict())
        else:
            return jsonify({ "error" : {"not found" : "the location is not found ok"}})



## HTTP POST - Create Record

@app.route("/add", methods = ["POST", "GET"])
def add():
    form = CafeForm()
    if request.method == "GET":
        return render_template("add.html", form=form)
    if request.method == "POST":
        cafe = Cafe(name=form.name.data, map_url=form.map_url.data, img_url=form.img_url.data, location=form.location.data, seats=form.seats.data, has_toilet=form.has_toilet.data,
                    has_sockets=form.has_sockets.data, has_wifi=form.has_wifi.data, can_take_calls=form.can_take_calls.data, coffee_price=form.coffee_price.data)
        db.session.add(cafe)
        db.session.commit()
        return redirect(url_for("home"))   
    

## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<cafe_id>", methods = ["PATCH","GET"])
def update_price(cafe_id):
        
        cafe = Cafe.query.filter_by(id = cafe_id).first() 
        if cafe: 
            cafe.coffee_price = request.args.get("new_price")
            db.session.commit()
            return jsonify({ "success" : "Entry updated"})
        else: 
            return jsonify({"error": "id not found ok"})    
        


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods = ["POST","GET"])
def delete(cafe_id):
        cafe = Cafe.query.filter_by(id = cafe_id).first() 
        if cafe:
            if request.args.get("api_key") == "TopSecretAPIKey":
                db.session.delete(cafe)
                db.session.commit()
                return jsonify({"success": "Cafe has been deleted"}) , 200
            else:
                return jsonify({"error" : "please enter correct API Key"}), 403
        else:
            return jsonify({"error" : "please enter a correct ID"}), 404

if __name__ == '__main__':
    app.run(debug=True)
