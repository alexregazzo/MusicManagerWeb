import React, { createContext, useState } from "react";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [userId, setUserId] = useState(null);
  // const [username, setUsername] = useState(null);

  return <AuthContext.Provider value={{ signedIn: !!userId, setUserId, userId }}>{children}</AuthContext.Provider>;
};

export default AuthContext;
