import pytest
from learn_flask import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200
    # assert resp.text = "someting"

def test_predict(client):
    test_data = {"CGPA": 9.24, "GRE": 330, "TOEFL": 114, "University_Rating": 3, "Research": 0, "LOR": 4.5}
    resp = client.post("/learn/jamboree", json=test_data)
    assert resp.status_code == 200
    assert resp.text == "Your Admission chance is: 84.06 %"