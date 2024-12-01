
import React from 'react';
import { Link } from 'react-router-dom';

const NotFoundPage = () => {
  return (
    <div className="flex flex-col items-center h-screen text-center pt-[200px]">
      <div className="text-2xl font-bold">404</div>
      <div className="mb-4">The page you are looking for does not exist.</div>
      <Link to="/" className="text-blue-500 hover:underline">
        Go Back
      </Link>
    </div>
  );
};

export default NotFoundPage;