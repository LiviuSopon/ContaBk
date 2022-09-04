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
        expected = b'[{"email":"test_email_1","name":"test_name_1","phone":"test_phone_1"}]\n'  # noqa: E501
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
        expected = b'{"email":"test_email_1","name":"test_name_1","phone":"test_phone_1"}\n'  # noqa: E501
        assert expected == req.data
        assert req.status_code == 201


class TestDeletingData(BaseCase):
    def test_delete(self):
        test_contact = Contact(
            name="test_name_1", email="test_email_1", phone="test_phone_1"
        )
        with self.app.app_context():
            self.db.session.add(test_contact)
            self.db.session.commit()
        req = self.client.delete("/test_phone_1", json={})
        expected = b'{"result":true}\n'
        assert expected == req.data
        assert req.status_code == 200


class TestUpdatingData(BaseCase):
    def test_put(self):
        test_contact = Contact(
            name="test_name_1", email="test_email_1", phone="test_phone_1"
        )
        with self.app.app_context():
            self.db.session.add(test_contact)
            self.db.session.commit()
        req = self.client.put("/test_phone_1", json={"name": "test_name_2"})
        expected = b'{"email":"test_email_1","name":"test_name_2","phone":"test_phone_1"}\n'  # noqa: E501
        assert expected == req.data
        assert req.status_code == 200
