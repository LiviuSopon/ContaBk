from . import db


class Contact(db.Model):
    """
    Basic database model for a contact.
    The id autoincrements.
    The only other unique column is the phone number, because only one person
    can have a certain phone number.
    """

    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False, unique=True)

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }
