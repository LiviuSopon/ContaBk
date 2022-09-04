# import json

from BaseCase import BaseCase
from src.models import Contact  # noqa: E402


class TestReadingData(BaseCase):
    def test_get(self):
        test_contact = Contact(
            name="test_name_1", email="test_email_1", phone="test_phone_1"
        )
        with self.app.app_context():
            self.db.session.add(test_contact)
            self.db.session.commit()
        req = self.client.get("/all", json={})
        expected = b'[{"email":"test_email_1","name":"test_name_1","phone":"test_phone_1"}]\n'
        print(req.data)
        assert expected == req.data
        assert req.status_code == 200


class TestAddingData(BaseCase):
    def test_post(self):
        req = self.client.post(
            "/add",
            json={
                "name": "test_name_1",
                "email": "test_email_1",
                "phone": "test_phone_1",
            },
        )
        print(req.data)
        print("status: ", req.status_code)
