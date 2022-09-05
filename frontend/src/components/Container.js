import React, { useState, useEffect } from "react";
import AddForm from "./AddForm";
import Contact from "./Contact";
import "../style/styles.css";

const Container = () => {
  const [contacts, setContacts] = useState([]);
  const [trigger, setTrigger] = useState(false);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/all")
      .then((response) => response.json())
      .then((data) => {
        setContacts(data);
      })
      .catch((err) => {
        console.log(err.message);
      });
  }, []);

  if (trigger) {
    return (
      <>
        <AddForm
          contacts={contacts}
          setContacts={setContacts}
          setTrigger={setTrigger}
        />
      </>
    );
  } else {
    return (
      <div>
        <button id="add" onClick={() => setTrigger(true)}>
          Add
        </button>
        <div className="container">
          {contacts.map((contact) => (
            <Contact
              key={contact.phone}
              name={contact.name}
              email={contact.email}
              phone={contact.phone}
              setContacts={setContacts}
              contacts={contacts}
            />
          ))}
        </div>
      </div>
    );
  }
};

export default Container;
