import React, { useState } from "react";
import "../style/styles.css";

const AddForm = (props) => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");

  const addContacts = async (name, email, phone) => {
    await fetch("http://127.0.0.1:5000/add", {
      method: "POST",
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
        props.setContacts((contacts) => [...contacts, data]);
        setName("");
        setEmail("");
        setPhone("");
      })
      .catch((err) => {
        console.log(err.message);
      });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    addContacts(name, email, phone);
    props.setTrigger(false);
  };

  return (
    <div>
      <form onSubmit={handleSubmit} id="addForm" className="card">
        <input
          placeholder="Name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          placeholder="Email"
          type="text"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          placeholder="Phone"
          type="text"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
        />
        <button type="submit">Save</button>
        <button onClick={() => props.setTrigger(false)}>Back</button>
      </form>
    </div>
  );
};

export default AddForm;
