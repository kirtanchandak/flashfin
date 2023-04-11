import { useState } from "react";
import "./App.css";

function App() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    mobile: "",
  });

  let name, value;
  const postData = (e) => {
    name = e.target.name;
    value = e.target.value;

    setForm({ ...form, [name]: value });
  };

  const submitData = async (e) => {
    e.preventDefault();
    const { name, email, mobile } = form;
    const res = fetch(
      "https://flashfin-4b7a6-default-rtdb.firebaseio.com/userData.json",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name,
          email,
          mobile,
        }),
      }
    );
    if (res) {
      setForm({
        name: "",
        email: "",
        mobile: "",
      });
      alert("Data Stored");
    } else {
      alert("Please fill the data");
    }
  };
  return (
    <div className="App">
      <form action="">
        <label htmlFor="">Name</label>
        <input
          type="text"
          placeholder="enter name"
          value={form.name}
          name="name"
          onChange={postData}
        />{" "}
        <br />
        <label htmlFor="">Email</label>
        <input
          type="text"
          placeholder="enter email"
          value={form.email}
          name="email"
          onChange={postData}
        />
        <br />
        <label htmlFor="">Mobile</label>
        <input
          type="text"
          placeholder="enter mobile"
          value={form.mobile}
          name="mobile"
          onChange={postData}
        />
        <button type="submit" onClick={submitData}>
          Submit
        </button>
      </form>
    </div>
  );
}

export default App;
