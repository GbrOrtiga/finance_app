import requests

BASE_URL = "http://127.0.0.1:5000"

# Criar usuário
res = requests.post(f"{BASE_URL}/users/", json={
    "name": "Teste",
    "email": "teste@email.com"
})
print("Usuário:", res.json())

# Criar categoria
res = requests.post(f"{BASE_URL}/categories/", json={
    "name": "Teste Categoria"
})
print("Categoria:", res.json())

# Criar transação
res = requests.post(f"{BASE_URL}/transactions/", json={
    "user_id": 1,
    "category_id": 1,
    "amount": 50,
    "type": "entrada"
})
print("Transação:", res.json())