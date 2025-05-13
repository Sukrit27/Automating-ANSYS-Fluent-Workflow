// Home.js
import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import AOS from "aos";
import "aos/dist/aos.css";
import "./Home.css";

import topView from "../assets/top_view.jpg";
import frontView from "../assets/front_view.jpg";
import sideView from "../assets/side_view.jpg";
import contourImg from "../assets/3d5000.png";
import savedImg from "../assets/lossplot.jpg";
import geom from "../assets/3d_geometry.jpg";

function Home() {
  const navigate = useNavigate();

  useEffect(() => {
    AOS.init({ duration: 1000 });
  }, []);

  return (
    <div className="home">
      {/* HERO */}
      <section className="hero" data-aos="fade-up">
        <h1>Problem Statement</h1>
        <p>
          Automating ANSYS Fluent workflows using PyFluent and a modern web
          interface. This project aims to simplify complex simulation processes,
          reduce manual errors, and provide engineers with a seamless
          visualization and analysis experience.
        </p>
        <span className="scroll-down">⌄</span>
      </section>

      {/* VISUALIZATION */}
      <section className="visualization-section" data-aos="fade-up">
        <div className="description">
          <h2>Geometry Visualization</h2>
          <p>
            Here's a 3D representation of the geometry used in our simulation.
            This helps better understand structure and boundary conditions
            applied in ANSYS Fluent for CFD analysis.
          </p>
        </div>
        <div className="visual">
          <iframe
            src={geom}
            title="3D Geometry"
            frameBorder="0"
            allowFullScreen
          />
        </div>
      </section>

      {/* OUR MODEL */}
      <section className="model-section" data-aos="fade-up">
      <h2>Our Model</h2>
      <div className="model-images">
        <div
          className="image-card"
          onClick={() => window.open(topView, "_blank")}
        >
          <img src={topView} alt="Top View" />
          <p className="image-title">Top View</p>
        </div>
        <div
          className="image-card"
          onClick={() => window.open(frontView, "_blank")}
        >
          <img src={frontView} alt="Front View" />
          <p className="image-title">Front View</p>
        </div>
        <div
          className="image-card"
          onClick={() => window.open(sideView, "_blank")}
        >
          <img src={sideView} alt="Side View" />
          <p className="image-title">Side View</p>
        </div>
      </div>
    </section>

      {/* SAVED RESULTS */}
      <section className="results-section" data-aos="fade-up">
        <h2>Saved Results</h2>
        <div className="results-images">
          <div
            className="image-box"
            onClick={() => navigate("/contour-plots")}
          >
            <img src={contourImg} alt="Contour Preview" />
            <div className="overlay">Contour Plots</div>
          </div>
          <div
            className="image-box"
            onClick={() => navigate("/graph-plots")}
          >
            <img src={savedImg} alt="Graph Preview" />
            <div className="overlay">Graph Plots</div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;
