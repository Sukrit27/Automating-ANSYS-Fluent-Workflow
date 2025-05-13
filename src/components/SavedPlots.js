import React from "react";
import "./SavedPlots.css";
import sim_results from "../assets/sim_results.jpg";
import temp from "../assets/tempplot.jpg";
import loss from "../assets/lossplot.jpg";
import ohm from "../assets/ohmplot.jpg";

export default function SavedPlots() {
  const plots = [
    { src: temp, alt: "Temperature Distribution", title: "Temperature Distribution" },
    { src: loss, alt: "RPM vs Iron Loss", title: "RPM vs Iron Loss" },
    { src: ohm, alt: "RPM vs Ohmic Loss", title: "RPM vs Ohmic Loss" },
  ];

  return (
    <div className="saved-plots-container">
      <h1 className="main-heading">Obtained Results</h1>

      <div className="result-section">
        <div className="result-image">
          <img src={sim_results} alt="Simulation Result" />
        </div>
        <div className="result-description">
          <p>
          The “Obtained Results” section presents five distinct simulation outputs—each corresponding to a different rotor speed (3 000 RPM, 4 000 RPM, 5 000 RPM, 6 000 RPM, and 7 000 RPM). As you can see in the image above, each case highlights the temperature and flow distributions within the motor geometry, allowing for a clear comparison of how increasing RPM affects thermal and fluid‐dynamic behavior.

Of course, the total number of simulations can be tailored to your specific needs—simply select as many RPM values as required. Below, you’ll find the corresponding graphs for these results, providing a quantitative view of key performance metrics (e.g., temperature rise, ohmic and iron losses) across the different operating speeds.
          </p>
        </div>
      </div>

      <h2 className="sub-heading">Plots</h2>
      <div className="plot-gallery">
        {plots.map((plot, idx) => (
          <div
            key={idx}
            className="plot-item"
            onClick={() => window.open(plot.src, "_blank")}
          >
            <img src={plot.src} alt={plot.alt} />
            <p>{plot.title}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
