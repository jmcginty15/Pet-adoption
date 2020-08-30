"""Pet adoption application."""

from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yeet'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)
db.create_all()

@app.route('/')
def home():
    """List all pets in database"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/<group>')
def show_groups(group):
    """Show pets by group, either available or not available"""
    if group == 'available':
        pets = Pet.query.filter_by(available=True).all()
    elif group == 'not-available':
        pets = Pet.query.filter_by(available=False).all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    """Form for adding new pet"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f'{name} added!')

        return redirect('/')
    else:
        return render_template('pet-form.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_details(pet_id):
    """Display pet details and edit form"""
    pet = Pet.query.get(pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f'{pet.name} updated!')
        return redirect(f'/{pet_id}')
    else:
        return render_template('pet-details.html', pet=pet, form=form)