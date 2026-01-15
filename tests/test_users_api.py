from utils.api_client import get_users, get_single_user, create_user


def test_get_users_success():
    response = get_users(page=1)
    assert response.status_code == 200
    assert "data" in response.json()


def test_get_single_user_success():
    response = get_single_user(user_id=2)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2


def test_get_single_user_not_found():
    response = get_single_user(user_id=999)
    assert response.status_code == 404


def test_create_user_success():
    response = create_user(name="Dorian", job="QA Engineer")
    assert response.status_code == 201
    assert "id" in response.json()
