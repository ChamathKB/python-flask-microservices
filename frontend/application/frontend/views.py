from django import forms
from numpy import product
import requests
from . import forms
from . import frontend_blueprint
from .. import login_manager
from .api.UserClient import UserClient
from .api.ProductClient import ProductClient
from .api.OrderClient import OrederClient
from flask import render_template, session, redirect, url_for, flash, request
from flask_login import current_user

@login_manager.user_loader
def load_user(user_id):
    return None

@frontend_blueprint.route('/', methods='GET')
def home():
    if current_user.is_authenticated:
        session['order'] = OrederClient.get_order_from_session()

    try:
        products = ProductClient.get_product()
    except requests.exceptions.ConnectionError:
        product = {
            'result': []
        }

    return render_template('home/index.html', products=products)

@frontend_blueprint.route('/register', method=['GET', 'POST'])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validation_on_submit():
            username = form.username.data

            user = UserClient.does_exist(username)
            if user:
                flash(['Please try another username', 'error'])
                return render_template('register/index.html', form=form)
            else:
                user = UserClient.post_user_create(form)
                if user:
                    flash('Thanks for registering, please login', 'success')
                    return redirect(url_for('frontend.login'))
    else:
        flash('Errors found', 'error')

        