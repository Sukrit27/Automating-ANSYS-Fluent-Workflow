import React, { useState } from "react";
import axios from "axios";
import "./LiveSimulation.css";

function LiveSimulation() {
  const [numRpms, setNumRpms] = useState(1);
  const [rpmList, setRpmList] = useState([""]);
  const [powList, setPowList] = useState([""]);
  const [ipowList, setiPowList] = useState([""]);
  // const [velocityX, setVelocityX] = useState("");
  // const [velocityY, setVelocityY] = useState("");
  // const [velocityZ, setVelocityZ] = useState("");
  const [results, setResults] = useState([]);
  // const [plotUrl, setPlotUrl] = useState(null);
  const [graphUrl, setGraphUrl] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleNumRpmsChange = (e) => {
    const n = parseInt(e.target.value, 10) || 0;
    setNumRpms(n);
    setRpmList(Array(n).fill(""));
    setPowList(Array(n).fill(""));
    setiPowList(Array(n).fill(""));
    
  };

  const handleRpmChange = (index) => (e) => {
    const newList = [...rpmList];
    newList[index] = e.target.value;
    setRpmList(newList);
  };
  const handlePowChange = (index) => (e) => {
    const newList = [...powList];
    newList[index] = e.target.value;
    setPowList(newList);
  };
  const handleiPowChange = (index) => (e) => {
    const newList = [...ipowList];
    newList[index] = e.target.value;
    setiPowList(newList);
  };

  const runSimulation = async () => {
    setLoading(true);
    try {
      const payload = {
        rpms: rpmList.map((v) => parseFloat(v)),
        pows: powList.map((v) => parseFloat(v)),
        ipows: ipowList.map((v) => parseFloat(v)),
        // velocityX: parseFloat(velocityX),
        // velocityY: parseFloat(velocityY),
        // velocityZ: parseFloat(velocityZ),
      };

      const response = await axios.post("http://localhost:5000/run_simulation", payload);
      const data = response.data;

      if (data.results) {
        setResults(data.results);
        // if (data.contour_file_base) {
        //   setPlotUrl(data.contour_file_base);
        // }
        if (data.graph_url) {
          setGraphUrl(data.graph_url);
        }
      }

      alert("Simulation Completed!");
    } catch (error) {
      console.error("Error running simulation:", error);
      alert("Simulation failed!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>ANSYS Simulation</h1>

      <div className="section">
        <h2>How many RPM values?</h2>
        <input type="number" min="1" value={numRpms} onChange={handleNumRpmsChange} />
      </div>

      <div className="section parameters">
        {rpmList.map((val, idx) => (
          <div key={idx} className="parameter-box">
            <h3>{`RPM ${idx + 1} (rev/min)`}</h3>
            <input type="number" value={val} onChange={handleRpmChange(idx)} />
          </div>
        ))}
      </div>

      <div className="section parameters">
        {powList.map((val, idx) => (
          <div key={idx} className="parameter-box">
            <h3>{`Ohmic Loss ${idx + 1} (W/m^3)`}</h3>
            <input type="number" value={val} onChange={handlePowChange(idx)} />
          </div>
        ))}
      </div>

      <div className="section parameters">
        {ipowList.map((val, idx) => (
          <div key={idx} className="parameter-box">
            <h3>{`Iron Loss ${idx + 1} (W/m^3)`}</h3>
            <input type="number" value={val} onChange={handleiPowChange(idx)} />
          </div>
        ))}
      </div>

      {/* <div className="section">
        <h2>Translational Velocity</h2>
        <div className="parameters">
          <div className="parameter-box">
            <label>X:</label>
            <input type="number" value={velocityX} onChange={(e) => setVelocityX(e.target.value)} />
          </div>
          <div className="parameter-box">
            <label>Y:</label>
            <input type="number" value={velocityY} onChange={(e) => setVelocityY(e.target.value)} />
          </div>
          <div className="parameter-box">
            <label>Z:</label>
            <input type="number" value={velocityZ} onChange={(e) => setVelocityZ(e.target.value)} />
          </div>
        </div>
      </div> */}

      <button className="run-button" onClick={runSimulation} disabled={loading}>
        {loading ? "Running Simulation..." : "Run Simulation"}
      </button>

      {/* Results Display */}
      {results.length > 0 && (
        <div className="section results-container">
          <h2>Results</h2>
          {results.map((res, idx) => (
            <div key={idx} className="result-box">
              <strong>RPM:</strong> {res.rpm} &nbsp;|&nbsp; <strong>Ohmic Loss:</strong> {res.pow} &nbsp;|&nbsp; <strong>Iron Loss:</strong> {res.ipow} &nbsp;|&nbsp; <strong>Avg Temp:</strong> {res.temperature_result.toFixed(2)}
            </div>
          ))}
        </div>
      )}

      {/* {plotUrl && (
        <div className="section plot-container">
          <h2>Contour Plot</h2>
          <iframe src={plotUrl} width="100%" height="600px" title="Contour Plot" />
        </div>
      )} */}

      {graphUrl && (
        <div className="section graph-container">
          <h2>Temperature vs RPM Graph</h2>
          <img src={graphUrl} alt="Temperature vs RPM" style={{ width: "100%" }} />
        </div>
      )}
    </div>
  );
}

export default LiveSimulation;