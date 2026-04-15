def validate_transaction(data):
    errors = []

    amount = data.get("amount")
    if amount is None or float(amount) <= 0:
        errors.append("O valor deve ser positivo.")

    type_ = data.get("type")
    if type_ not in ("entrada", "saida"):
        errors.append("O tipo deve ser 'entrada' ou 'saida'.")

    if not data.get("category_id"):
        errors.append("A categoria é obrigatória.")

    if not data.get("user_id"):
        errors.append("O usuário é obrigatório.")

    return errors