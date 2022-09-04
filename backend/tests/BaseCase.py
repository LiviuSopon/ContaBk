import unittest
import os

os.environ["FLASK_CONFIG"] = "testing"
os.environ["TEST_DATABASE_URL"] = "sqlite:///{}/tests/testing.db".format(
    os.getcwd()
)

from src.routes import app  # noqa: F401,E402
from src import db  # noqa: E402


class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = app.test_client()
        self.db = db

    def tearDown(self):
        with app.app_context():
            self.db.drop_all()
