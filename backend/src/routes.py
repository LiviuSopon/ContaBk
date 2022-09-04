import os
from . import create_app
from . import db
from .models import Contact
from flask import jsonify
from flask import request
from flask import abort

app = create_app(os.getenv("FLASK_CONFIG") or "default")


@app.route("/add", methods=["POST"])
def create_contact():
    if not request.json:
        abort(400)  # noqa: F821
    contact = Contact(
        name=request.json.get("name"),
        email=request.json.get("email"),
        phone=request.json.get("phone"),
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify(contact.to_json()), 201


@app.route("/all", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([contact.to_json() for contact in contacts])


@app.route("/<phone>", methods=["DELETE"])
def delete_contact(phone):
    contact = Contact.query.filter_by(phone=phone).first()
    if contact is None:
        abort(404)  # noqa: F821
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"result": True})


@app.route("/<phone>", methods=["PUT"])
def update_contact(phone):
    if not request.json:
        abort(400)  # noqa: F821
    contact = Contact.query.get(phone)
    if contact is None:
        abort(404)  # noqa: F821
    contact.name = request.json.get("name", contact.name)
    contact.email = request.json.get("email", contact.email)
    contact.phone = request.json.get("phone", contact.phone)
    db.session.commit()
    return jsonify(contact.to_json())
