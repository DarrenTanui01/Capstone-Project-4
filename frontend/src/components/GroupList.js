import React, { useEffect, useState } from "react";
import { getGroups } from "../api";

export default function GroupList({ token }) {
  const [groups, setGroups] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    console.log("Token being sent to getGroups:", token); // Add this line
    getGroups(token).then(data => {
      if (Array.isArray(data)) {
        setGroups(data);
        setError("");
      } else {
        setGroups([]);
        setError(data.error || "Failed to load groups.");
      }
    });
  }, [token]);

  return (
    <div>
      <h3>Your Groups</h3>
      {error && <div style={{color: "red"}}>{error}</div>}
      <ul>
        {groups.map(g => (
          <li key={g.id}>{g.name} - {g.description}</li>
        ))}
      </ul>
    </div>
  );
}