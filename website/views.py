from flask import Blueprint, render_template, request, session, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import random

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/techsiulutions')
def techsiulutions():
    return render_template("index.html")

@views.route('/photos')
def photos():
    return render_template("photos.html")

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/number')
def number():
    session["number"] = random.randrange(0,30)
    print(session["number"])
    return render_template("number.html")

@views.route('/guess', methods=['POST'])
def result():
    if int(request.form['guess']) == session['number']:
        answer = "Correct"
        return render_template("number.html", answer=answer)
    elif int(request.form['guess']) < session['number']:
        answer = "It's too Low"
        return render_template("number.html", answer=answer)
    else:
        answer = "It's too High"
        return render_template("number.html", answer=answer)