from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'somemoregoodfun'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
sess = db.session

@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def show_add_pet_form():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        sess.add(new_pet)
        sess.commit()
        return redirect("/")
    else:
        return render_template("addPetForm.html", form=form)

@app.route('/<int:pet_id>',  methods=["GET", "POST"])
def show_pet_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        sess.add(pet)
        sess.commit()
        return redirect('/')
    else:
        return render_template("displayPet.html", pet=pet, form=form)