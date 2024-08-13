import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.fixture
def auto_from_db():
    auto = {
        "vin_code": "XTA00202121",
        "mark": "Audi",
        "model": "Q8",
        "year": 2020,
        "mileage": 20000,
        "id": 1,
        "client": {
            "first_name": "Боря",
            "last_name": "Бритва",
            "phone_number": "8 (919) 543-05-72",
            "id": 1
        }
    }
    return auto


class TestAutoRouter:

    def test_get_all_auto():
        response = client.get('/auto')
        assert response.status_code == 200
