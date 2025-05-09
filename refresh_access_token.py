import requests
import json

# Замените на свой логин и пароль
USERNAME = "superuser"
PASSWORD = "1643adg12"

TOKEN_URL = "http://127.0.0.1:8000/api/token/"
TOKENS_FILE = "tokens.json"

def get_tokens(username, password):
    data = {"username": username, "password": password}
    response = requests.post(TOKEN_URL, json=data)

    if response.status_code == 200:
        tokens = response.json()
        with open(TOKENS_FILE, "w") as f:
            json.dump(tokens, f, indent=4)
        print("✅ Токены успешно обновлены и сохранены в tokens.json")
    else:
        print("❌ Ошибка получения токенов:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    get_tokens(USERNAME, PASSWORD)
