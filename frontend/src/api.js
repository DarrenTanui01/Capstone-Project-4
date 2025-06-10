const API_BASE = "http://127.0.0.1:5000";

export async function signup(data) {
  const res = await fetch(`${API_BASE}/auth/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function login(data) {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function getGroups(token) {
  const res = await fetch(`${API_BASE}/api/groups`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return res.json();
}

export async function createGroup(data, token) {
  const res = await fetch(`${API_BASE}/api/groups`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function depositSavings(data, token) {
  const res = await fetch(`${API_BASE}/api/savings`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
    body: JSON.stringify(data),
  });
  return res.json();
}