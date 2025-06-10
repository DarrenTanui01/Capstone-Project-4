import React, { useState } from "react";
import { login } from "../api";

export default function Login({ setToken }) {
  const [form, setForm] = useState({ username: "", password: "" });
  const [msg, setMsg] = useState("");

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    const res = await login(form);
    if (res.access_token) {
      setToken(res.access_token);
      localStorage.setItem("token", res.access_token);
      setMsg("");
    } else {
      setMsg(res.error || "Login failed.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Log In</h2>
      <input name="username" placeholder="Username" onChange={handleChange} required />
      <input name="password" type="password" placeholder="Password" onChange={handleChange} required />
      <button type="submit">Log In</button>
      <div>{msg}</div>
    </form>
  );
}