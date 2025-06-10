import React, { useState } from "react";
import { depositSavings } from "../api";

export default function DepositSavings({ token }) {
  const [form, setForm] = useState({ group_id: "", amount: "" });
  const [msg, setMsg] = useState("");

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    const res = await depositSavings({ ...form, amount: parseFloat(form.amount) }, token);
    console.log("Deposit savings response:", res);
    if (res.id) setMsg("Deposit successful!");
    else setMsg(res.error || "Deposit failed.");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Deposit Savings</h3>
      <input name="group_id" placeholder="Group ID" onChange={handleChange} required />
      <input name="amount" type="number" placeholder="Amount" onChange={handleChange} required />
      <button type="submit">Deposit</button>
      <div>{msg}</div>
    </form>
  );
}