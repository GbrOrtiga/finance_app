from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from app.models import Category
from app.models import Transaction, Log

categories_bp = Blueprint("categories", __name__)

@categories_bp.route("/", methods=["GET"])
def list_categories():
    cats = Category.query.all()
    return jsonify([{"id": c.id, "name": c.name} for c in cats])

@categories_bp.route("/", methods=["POST"])
def create_category():
    data = request.get_json()

    cat = Category(name=data["name"], description=data.get("description"))
    db.session.add(cat)
    db.session.commit()

    return {"id": cat.id, "name": cat.name}, 201