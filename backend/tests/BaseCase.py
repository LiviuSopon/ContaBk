import unittest
import os

# Set the environment variables required for testing.
os.environ["FLASK_CONFIG"] = "testing"
os.environ["TEST_DATABASE_URL"] = "sqlite:///{}/tests/testing.db".format(
    os.getcwd()
)

# Noqa to ignore the warning with top level commits.
# We need to set the variables before importing the app.
from src.routes import app  # noqa: F401,E402
from src import db  # noqa: E402


class BaseCase(unittest.TestCase):
    """
    Base class from which all tests will inherit.
    For the setup it creates the database and sets the corresponding variables.
    For the teardown, it deletes all of the info in the database,
    for clean testing each time.
    """

    def setUp(self):
        self.app = app
        self.client = app.test_client()
        self.db = db
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            self.db.drop_all()
