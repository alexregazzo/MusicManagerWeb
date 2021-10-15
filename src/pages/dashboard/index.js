import React, { useContext, useEffect, useState } from "react";

import AuthContext from "../../context/auth";

function Dashboard() {
  const { signedIn, userId, setUserId } = useContext(AuthContext);
  const [formUsername, setFormUsername] = useState("");
  const [formPassword, setFormPassword] = useState("");
  const [isConnected, setIsConnected] = useState(null);
  const [connectSpotifyUrl, setConnectSpotifyUrl] = useState(null);

  useEffect(isconnectedSpotify, [userId]);

  function isconnectedSpotify() {
    if (!userId) return;
    fetch(`/api/v0/spotify/isconnected?id=${userId}`, {
      method: "GET",
    })
      .then((r) => {
        if (r.ok) {
          return r.json();
        }
        return {};
      })
      .then((data) => {
        setIsConnected(data["is_connected"]);
        setConnectSpotifyUrl(data["connect_link"]);
      });
  }

  function cadastrar() {
    fetch("/api/v0/account/signup", {
      method: "POST",
      body: JSON.stringify({
        username: formUsername,
        password: formPassword,
      }),
    })
      .then((r) => {
        if (r.ok) {
          return r.json();
        }
        return {};
      })
      .then((data) => {
        setUserId(data["use_id"]);
      });
  }
  function entrar() {
    fetch("/api/v0/account/login", {
      method: "POST",
      body: JSON.stringify({
        username: formUsername,
        password: formPassword,
      }),
    })
      .then((r) => {
        if (r.ok) {
          return r.json();
        }
        return {};
      })
      .then((data) => {
        console.log(data);
        setUserId(data["use_id"]);
      });
  }

  if (signedIn) {
    // Signed in
    console.log(userId);
    return (
      <div>
        {
          isConnected !== null && !isConnected && 
          <a href={connectSpotifyUrl}>Conectar ao Spotify</a>
        
        }
        <h2>Teste {userId}</h2>
      </div>
    );
  } else {
    // Not signed in
    return (
      <div>
        <form>
          <h3>Entrar/Cadastrar</h3>
          <label>Username:</label>
          <input type="text" onChange={(e) => setFormUsername(e.target.value)} />
          <label>Password:</label>
          <input type="password" onChange={(e) => setFormPassword(e.target.value)} />

          <button type="button" onClick={cadastrar}>
            Cadastrar
          </button>
          <button type="button" onClick={entrar}>
            Entrar
          </button>
        </form>
      </div>
    );
  }
}

export default Dashboard;
