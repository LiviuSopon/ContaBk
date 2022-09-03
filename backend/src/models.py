from . import db


class Contact(db.Model):
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
