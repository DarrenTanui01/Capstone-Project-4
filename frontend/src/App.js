import React, { useState } from "react";
import Signup from "./components/Signup";
import Login from "./components/Login";
import Dashboard from "./components/Dashboard";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || "");

  if (!token) {
    return (
      <div>
        <h1>Proxima Centauri</h1>
        <Signup setToken={setToken} />
        <Login setToken={setToken} />
      </div>
    );
}

  return <Dashboard token={token} setToken={setToken} />;
}

export default App;