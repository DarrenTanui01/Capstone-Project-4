import React, { useState } from "react";
import { signup } from "../api";

export default function Signup({ setToken }) {
  const [form, setForm] = useState({ username: "", email: "", password: "" });
  const [msg, setMsg] = useState("");

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    const res = await signup(form);
    if (res.message) setMsg("Signup successful! Please log in.");
    else setMsg(res.error || "Signup failed.");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Sign Up</h2>
      <input name="username" placeholder="Username" onChange={handleChange} required />
      <input name="email" placeholder="Email" onChange={handleChange} required />
      <input name="password" type="password" placeholder="Password" onChange={handleChange} required />
      <button type="submit">Sign Up</button>
      <div>{msg}</div>
    </form>
  );
}