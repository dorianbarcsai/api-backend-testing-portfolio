from utils.api_client import login


def test_login_success():
    response = login(
        email="eve.holt@reqres.in",
        password="cityslicka"
    )
    assert response.status_code == 200
    assert "token" in response.json()


def test_login_missing_password():
    response = login(
        email="eve.holt@reqres.in",
        password=""
    )
    assert response.status_code == 400
