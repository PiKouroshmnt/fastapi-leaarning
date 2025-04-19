import json
import pytest

def test_create_summary(test_app_with_db):
    response = test_app_with_db.post("/summaries/", data=json.dumps({"url": "https://foo.bar"}))

    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"

def test_create_summary_invalid_json(test_app_with_db):
    response = test_app_with_db.post("/summaries/", data=json.dumps({}))

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
            "type": "missing",
            "loc": [
                "body",
                "url"
            ],
            "msg": "Field required",
            "input": {},
            "url": "https://errors.pydantic.dev/2.11/v/missing"
            }
        ]
    }
