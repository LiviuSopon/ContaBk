import "../style/styles.css";
import React, { useState } from "react";

const Contact = (props) => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [modify, setModify] = useState(false);

  const deleteContact = async (phone) => {
    await fetch(`http://127.0.0.1:5000/${phone}`, {
      method: "DELETE",
    }).then((response) => {
      if (response.status === 200) {
        props.setContacts(
          props.contacts.filter((contact) => {
            return contact.phone !== phone;
          })
        );
      } else {
        return;
      }
    });
  };

  const modifyContact = async (name, email, phone) => {
    await fetch(`http://127.0.0.1:5000/${props.phone}`, {
      method: "PUT",
      body: JSON.stringify({
        name: name,
        email: email,
        phone: phone,
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        props.setContacts(
          props.contacts.filter((contact) => {
            return contact.phone !== props.phone;
          })
        );
        props.setContacts((contacts) => [data, ...contacts]);
      })
      .catch((err) => {
        console.log(err.message);
      });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    modifyContact(name, email, phone);
    setModify(false);
  };

  if (modify) {
    return (
      <div className="card">
        <form onSubmit={handleSubmit} className="card">
          <input
            placeholder={props.name}
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <input
            placeholder={props.email}
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            placeholder={props.phone}
            type="text"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
          <button type="submit">Save</button>
          <button onClick={() => setModify(false)}>Back</button>
        </form>
      </div>
    );
  } else {
    return (
      <div className="card">
        <p>{props.name}</p>
        <p>{props.email}</p>
        <p>{props.phone}</p>
        <button onClick={() => setModify(true)}>Modify</button>
        <button onClick={() => deleteContact(props.phone)}>Delete</button>
      </div>
    );
  }
};

export default Contact;
