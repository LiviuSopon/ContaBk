import React, { useState, useEffect } from "react";
import Contact from "./Contact";

const Container = () => {
  const [contacts, setContacts] = useState([]);

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

  return (
    <>
      <button>Add</button>
      {contacts.map((contact) => (
        <Contact
          key={contact.phone}
          name={contact.name}
          email={contact.email}
          phone={contact.phone}
        />
      ))}
    </>
  );
};

export default Container;
