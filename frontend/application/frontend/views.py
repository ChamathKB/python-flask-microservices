from django import forms
import requests
from . import forms
from . import frontend_blueprint
from .. import login_manager
from .api.UserClient import UserClient
from .api.ProductClient import ProductClient
from .api.OrderClient import OrederClient
from flask import render_template, session, redirect, url_for, flash, request
from flask_login import current_user