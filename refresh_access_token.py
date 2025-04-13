import json
import requests

def refresh_access_token():
    try:
        with open('tokens.json') as f:
            tokens = json.load(f)
    except FileNotFoundError:
        print("Файл tokens.json не найден.")
        return

    response = requests.post(
        'http://127.0.0.1:8000/api/token/refresh/',
        json={'refresh': tokens['refresh']}
    )

    print("Ответ сервера:", response.status_code, response.text)

    if response.status_code == 200:
        new_access = response.json().get('access')
        if new_access:
            tokens['access'] = new_access
            with open('tokens.json', 'w') as f:
                json.dump(tokens, f, indent=4)
            print("✅ Access token успешно обновлён!")
        else:
            print("❌ Не удалось получить новый access токен.")
    else:
        print("❌ Ошибка при обновлении токена.")

refresh_access_token()
