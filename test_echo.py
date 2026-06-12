import requests

BASE_URL = "https://postman-echo.com"

def test_get_with_query_params():
    params = {"search": "python testing", "page": 5, "sort": "desc"}
    
    response = requests.get(f"{BASE_URL}/get", params=params)
    
    assert response.status_code == 200
    data = response.json()
    
    # PostmanEcho возвращает параметры как строки
    expected_params = {"search": "python testing", "page": "5", "sort": "desc"}
    assert data["args"] == expected_params


def test_post_json_data():
    payload = {
        "name": "Иван Петров",
        "email": "ivan@yandex.ru",
        "age": 28
    }
    
    response = requests.post(f"{BASE_URL}/post", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["json"] == payload


def test_post_form_data():
    form_data = {"login": "testuser123", "password": "qwerty123"}
    
    response = requests.post(f"{BASE_URL}/post", data=form_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["form"] == form_data


def test_put_request():
    update_data = {"id": 100500, "status": "updated"}
    
    response = requests.put(f"{BASE_URL}/put", json=update_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["json"] == update_data


def test_custom_headers():
    headers = {"X-API-Key": "secret-key-12345", "User-Agent": "MyApp/2.0"}
    
    response = requests.get(f"{BASE_URL}/get", headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    returned_headers = data["headers"]
    
    assert returned_headers.get("x-api-key") == "secret-key-12345"
    assert returned_headers.get("user-agent") == "MyApp/2.0"