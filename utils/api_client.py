import requests

BASE_URL = "https://reqres.in/api"


def get_users(page=1):
    return requests.get(f"{BASE_URL}/users", params={"page": page})


def get_single_user(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}")


def create_user(name, job):
    return requests.post(
        f"{BASE_URL}/users",
        json={"name": name, "job": job}
    )


def login(email, password):
    return requests.post(
        f"{BASE_URL}/login",
        json={"email": email, "password": password}
    )
