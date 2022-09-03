import os
from . import create_app
from . import db
from models import Contact
from flask import jsonify
from flask import request

app = create_app(os.getenv("FLASK_CONFIG") or "default")


@app.route("/add", methods=["POST"])
def create_contact():
    if not request.json:
        abort(400)  # noqa: F821
    contact = Contact(
        id=request.json.get("id"),
        name=request.json.get("name"),
        email=request.json.get("email"),
        phone=request.json.get("phone"),
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify(contact.to_json()), 201
