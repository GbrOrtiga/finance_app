from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from app.models import Category
from app.models import Transaction, Log
from datetime import datetime

transactions_bp = Blueprint("transactions", __name__)

@transactions_bp.route("/", methods=["POST"])
def create_transaction():
    data = request.get_json()

    if data["amount"] <= 0:
        return {"erro": "Valor deve ser positivo"}, 400

    if data["type"] not in ["entrada", "saida"]:
        return {"erro": "Tipo inválido"}, 400

    tx = Transaction(
        user_id=data["user_id"],
        category_id=data["category_id"],
        amount=data["amount"],
        type=data["type"],
        description=data.get("description"),
        date=datetime.strptime(data.get("date", str(datetime.utcnow().date())), "%Y-%m-%d")
    )

    db.session.add(tx)
    db.session.commit()

    log = Log(action="CREATE", entity="Transaction", entity_id=tx.id)
    db.session.add(log)
    db.session.commit()

    return {"id": tx.id, "amount": tx.amount}, 201

@transactions_bp.route("/", methods=["GET"])
def list_transactions():
    txs = Transaction.query.all()
    return jsonify([{"id": t.id, "amount": t.amount} for t in txs])