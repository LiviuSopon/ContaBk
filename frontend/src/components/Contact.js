import "../style/contact.css";

const Contact = (props) => {
  return (
    <div className="contact">
      <p>{props.name}</p>
      <p>{props.email}</p>
      <p>{props.phone}</p>
      <button>Modify</button>
      <button>Delete</button>
    </div>
  );
};

export default Contact;
