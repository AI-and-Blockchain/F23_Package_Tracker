import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div>
      <h1 className="homeHeader">Welcome to Package Tracker</h1>
      <Link to="/addPage">
        <button>Add a Package</button>
      </Link>
      <Link to="/claimPage">
        <button>Claim a Package</button>
      </Link>
      <Link to="/viewPage">
        <button>View Details of a Package</button>
      </Link>
    </div>
  );
};

export default Home;