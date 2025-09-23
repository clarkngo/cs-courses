import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Login({ setToken }) {
  const [form, setForm] = useState({
    email: "",
    password: "",
  });
  const navigate = useNavigate();

  function updateForm(value) {
    return setForm((prev) => {
      return { ...prev, ...value };
    });
  }

  async function onSubmit(e) {
    e.preventDefault();
    const user = { ...form };

    const response = await fetch("http://localhost:5050/user/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(user),
    });

    const data = await response.json();

    if (response.ok) {
      setToken(data.token);
      localStorage.setItem("token", data.token);
      navigate("/");
    } else {
      console.log(data.message);
    }
  }

  return (
    <div>
      <h3>Login</h3>
      <form onSubmit={onSubmit}>
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            className="form-control"
            id="email"
            value={form.email}
            onChange={(e) => updateForm({ email: e.target.value })}
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            className="form-control"
            id="password"
            value={form.password}
            onChange={(e) => updateForm({ password: e.target.value })}
          />
        </div>
        <div className="form-group">
          <input
            type="submit"
            value="Login"
            className="btn btn-primary"
          />
        </div>
      </form>
    </div>
  );
}