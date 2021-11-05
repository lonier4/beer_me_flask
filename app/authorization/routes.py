from flask import Blueprint, render_template, redirect, request, url_for, jsonify, json
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

from app.models import db, User

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['POST'])
def signup():
    data = request.json

    if request.method == 'POST' and data['password']==data['confirmPassword']:
            new_user = User(data['username'], data['email'], data['password'])

            try:
                db.session.add(new_user)
                db.session.commit()
            except:
                return jsonify("Gotta be quicker than that! Username or email already exists")
            return jsonify("Success")
    return jsonify("Passwords do not match. Give it another try.")

@auth.route('/signin', methods=['POST'])
def signin():
    data = request.json
    if request.method == 'POST':
        email = data['email']
        password = data['password']

        user = User.query.filter_by(email=email).first()

        if user is None or not check_password_hash(user.password, password):
            return jsonify('Incorrect username or password. Please try again.')
        return jsonify({"message": "good job", "user": user.to_dict()})

@auth.route('/signout')
def signout():
    logout_user()
    flash('You are now signed out.', category='alert-info')
    return redirect(url_for('auth.signin'))