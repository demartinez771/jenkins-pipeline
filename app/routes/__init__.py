"""Routes module."""
from flask import Blueprint

main_bp = Blueprint('main', __name__)

from app.routes import views  # noqa
