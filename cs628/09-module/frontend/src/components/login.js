import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const Login = () => {
  const backendUrl = process.env.REACT_APP_BACKEND_URL;
  const { user, fetchUser } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    fetchUser(); // Fetch user session after login
    if (user) {
      navigate("/home"); // Redirect to home if already authenticated
    }
  }, [user, navigate]);

  return (
    <div>
      <h2>Login</h2>
      <a href={`${backendUrl}/auth/github`} className="btn btn-primary">
        Login with GitHub
      </a>
    </div>
  );
};

export default Login;
