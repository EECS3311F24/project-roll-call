import React, { useEffect, useState, ReactNode } from 'react';
import { Navigate } from 'react-router-dom';

interface ProtectedRouteProps {
    children: ReactNode;
}

const checkAuthStatus = async () => {
    try {
        const response = await fetch('http://localhost:5000/auth/status', {
            method: "GET",
            credentials: "include", // Include session cookies
        });
      const data = await response.json();
      // Return both authentication status and user details
      return {
        authenticated: data.authenticated,
        user: data.user || null, // Safely handle cases where "user" might be undefined
      };
    } catch (error) {
      console.error('Error checking auth status:', error);
      return {
        authenticated: false,
        user: null,
      };
    }
  };

function ProtectedRoute({ children }: ProtectedRouteProps) {
    const [authData, setAuthData] = useState({ authenticated: null, user: null });
  
    useEffect(() => {
      const fetchAuthData = async () => {
        const result = await checkAuthStatus();
        setAuthData(result);
      };
      fetchAuthData();
    }, []);
    console.log(authData)
    if (authData.authenticated === null) {
      // Optionally display a loading state while checking authentication
      return <div>Loading...</div>;
    }
  
    return authData.authenticated ? children : <Navigate to="/" />;
  }
  
export default ProtectedRoute;