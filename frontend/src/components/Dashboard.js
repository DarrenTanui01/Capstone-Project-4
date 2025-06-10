import React from "react";
import GroupList from "./GroupList";
import CreateGroup from "./CreateGroup";
import DepositSavings from "./DepositSavings";

export default function Dashboard({ token, setToken }) {
  return (
    <div>
      <h2>Dashboard</h2>
      <button onClick={() => { setToken(""); localStorage.removeItem("token"); }}>Logout</button>
      <CreateGroup token={token} />
      <GroupList token={token} />
      <DepositSavings token={token} />
    </div>
  );
}