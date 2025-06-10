import React, { useState } from "react";
import { createGroup } from "../api";

export default function CreateGroup({ token }) {
  const [form, setForm] = useState({ name: "", description: "" });
  const [msg, setMsg] = useState("");

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    const res = await createGroup(form, token);
    console.log("Create group response:", res);
    if (res.id) setMsg("Group created!");
    else setMsg(res.error || "Failed to create group.");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Create Group</h3>
      <input name="name" placeholder="Group Name" onChange={handleChange} required />
      <input name="description" placeholder="Description" onChange={handleChange} />
      <button type="submit">Create</button>
      <div>{msg}</div>
    </form>
  );
}