import React, { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import Navbar from "./components/navbar";
import RecordList from "./components/recordList";
import Edit from "./components/edit";
import Create from "./components/create";
import Login from "./components/Login";
import Signup from "./components/Signup";
import { getToken, removeToken } from "./utils/auth";

const App = () => {
  const [token, setToken] = useState(getToken());
  const navigate = useNavigate();

  useEffect(() => {
    setToken(getToken());
  }, []);

  const handleLogout = () => {
    removeToken();
    setToken(null);
    navigate("/login");
  };

  return (
    <div>
      <Navbar token={token} handleLogout={handleLogout} />
      <Routes>
        {token ? (
          <>
            <Route exact path="/" element={<RecordList />} />
            <Route path="/edit/:id" element={<Edit />} />
            <Route path="/create" element={<Create />} />
          </>
        ) : (
          <>
            <Route path="/login" element={<Login setToken={setToken} />} />
            <Route path="/signup" element={<Signup setToken={setToken} />} />
          </>
        )}
      </Routes>
    </div>
  );
};

export default App;