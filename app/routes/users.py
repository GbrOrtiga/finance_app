from flask import Blueprint, request, jsonify
from app import db
from app.models import User

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
def list_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name})

# 🔥 AQUI ESTÁ O MAIS IMPORTANTE
@users_bp.route("/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()

    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)

    db.session.commit()

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email
    })

@users_bp.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuário removido"})