// components/Navbar.js
import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  return (
    <nav className="navbar">
      <h2>Automating ANSYS Fluent Workflows</h2>
      <Link to="/live-simulation" className="nav-link">
        Live Simulation
      </Link>
    </nav>
  );
}

export default Navbar;
