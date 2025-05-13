// App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import ContourPlots from "./components/ContourPlots";
import SavedPlots from "./components/SavedPlots";
import LiveSimulation from "./components/LiveSimulation";
import "./App.css";

function App() {
  return (
    <div className="app-wrapper">
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/contour-plots" element={<ContourPlots />} />
        <Route path="/graph-plots" element={<SavedPlots />} />
        <Route path="/live-simulation" element={<LiveSimulation />} />
      </Routes>
            {/* … your existing routes and layout … */}

            <footer className="site-footer">
        <div className="footer-section contributors">
          <h3>Contributors</h3>
          <ul>
            <li>
              <a
                href="https://github.com/your-github-username-1"
                target="_blank"
                rel="noopener noreferrer"
              >
                Soham Amrutkar
              </a>
            </li>
            <li>
              <a
                href="https://github.com/your-github-username-2"
                target="_blank"
                rel="noopener noreferrer"
              >
                Sukrit Ghosh
              </a>
            </li>
            <li>
              <a
                href="https://github.com/your-github-username-3"
                target="_blank"
                rel="noopener noreferrer"
              >
                Saptarshi Das
              </a>
            </li>
            <li>
              <a
                href="https://github.com/your-github-username-3"
                target="_blank"
                rel="noopener noreferrer"
              >
                Swaraj Mishra
              </a>
            </li>
            <li>
              <a
                href="https://github.com/your-github-username-3"
                target="_blank"
                rel="noopener noreferrer"
              >
                Harsh Mittal
              </a>
            </li>
          </ul>
        </div>

        <div className="footer-section supervisors">
          <h3>Supervisors</h3>
          <ul>
            <li>Dr. Ashwani Assam</li>
            <li>Dr. Anirban Bhattacharya</li>
            <li>Dr. Atul Thakur</li>
          </ul>
        </div>

        <div className="footer-section copyright">
          <p>
            &copy; {new Date().getFullYear()} Automating ANSYS Fluent Workflows. All rights reserved.
          </p>
        </div>
      </footer>


    </Router>
    </div>
  );
}

export default App;




// import React, { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [numRpms, setNumRpms] = useState(1);
//   const [rpmList, setRpmList] = useState([""]);
//   const [powList, setPowList] = useState([""]);
//   // const [velocityX, setVelocityX] = useState("");
//   // const [velocityY, setVelocityY] = useState("");
//   // const [velocityZ, setVelocityZ] = useState("");
//   const [results, setResults] = useState([]);
//   // const [plotUrl, setPlotUrl] = useState(null);
//   const [graphUrl, setGraphUrl] = useState(null);
//   const [loading, setLoading] = useState(false);

//   const handleNumRpmsChange = (e) => {
//     const n = parseInt(e.target.value, 10) || 0;
//     setNumRpms(n);
//     setRpmList(Array(n).fill(""));
//     setPowList(Array(n).fill(""));
//   };

//   const handleRpmChange = (index) => (e) => {
//     const newList = [...rpmList];
//     newList[index] = e.target.value;
//     setRpmList(newList);
//   };
//   const handlePowChange = (index) => (e) => {
//     const newList = [...powList];
//     newList[index] = e.target.value;
//     setPowList(newList);
//   };

//   const runSimulation = async () => {
//     setLoading(true);
//     try {
//       const payload = {
//         rpms: rpmList.map((v) => parseFloat(v)),
//         pows: powList.map((v) => parseFloat(v)),
//         // velocityX: parseFloat(velocityX),
//         // velocityY: parseFloat(velocityY),
//         // velocityZ: parseFloat(velocityZ),
//       };

//       const response = await axios.post("http://localhost:5000/run_simulation", payload);
//       const data = response.data;

//       if (data.results) {
//         setResults(data.results);
//         // if (data.contour_file_base) {
//         //   setPlotUrl(data.contour_file_base);
//         // }
//         if (data.graph_url) {
//           setGraphUrl(data.graph_url);
//         }
//       }

//       alert("Simulation Completed!");
//     } catch (error) {
//       console.error("Error running simulation:", error);
//       alert("Simulation failed!");
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="container">
//       <h1>ANSYS Simulation</h1>

//       <div className="section">
//         <h2>How many RPM values?</h2>
//         <input type="number" min="1" value={numRpms} onChange={handleNumRpmsChange} />
//       </div>

//       <div className="section parameters">
//         {rpmList.map((val, idx) => (
//           <div key={idx} className="parameter-box">
//             <h3>{`RPM ${idx + 1}`}</h3>
//             <input type="number" value={val} onChange={handleRpmChange(idx)} />
//           </div>
//         ))}
//       </div>

//       <div className="section parameters">
//         {powList.map((val, idx) => (
//           <div key={idx} className="parameter-box">
//             <h3>{`Power ${idx + 1}`}</h3>
//             <input type="number" value={val} onChange={handlePowChange(idx)} />
//           </div>
//         ))}
//       </div>

//       {/* <div className="section">
//         <h2>Translational Velocity</h2>
//         <div className="parameters">
//           <div className="parameter-box">
//             <label>X:</label>
//             <input type="number" value={velocityX} onChange={(e) => setVelocityX(e.target.value)} />
//           </div>
//           <div className="parameter-box">
//             <label>Y:</label>
//             <input type="number" value={velocityY} onChange={(e) => setVelocityY(e.target.value)} />
//           </div>
//           <div className="parameter-box">
//             <label>Z:</label>
//             <input type="number" value={velocityZ} onChange={(e) => setVelocityZ(e.target.value)} />
//           </div>
//         </div>
//       </div> */}

//       <button className="run-button" onClick={runSimulation} disabled={loading}>
//         {loading ? "Running Simulation..." : "Run Simulation"}
//       </button>

//       {/* Results Display */}
//       {results.length > 0 && (
//         <div className="section results-container">
//           <h2>Results</h2>
//           {results.map((res, idx) => (
//             <div key={idx} className="result-box">
//               <strong>RPM:</strong> {res.rpm} &nbsp;|&nbsp; <strong>Power:</strong> {res.pow} &nbsp;|&nbsp; <strong>Avg Temp:</strong> {res.temperature_result.toFixed(2)}
//             </div>
//           ))}
//         </div>
//       )}

//       {/* {plotUrl && (
//         <div className="section plot-container">
//           <h2>Contour Plot</h2>
//           <iframe src={plotUrl} width="100%" height="600px" title="Contour Plot" />
//         </div>
//       )} */}

//       {graphUrl && (
//         <div className="section graph-container">
//           <h2>Temperature vs RPM Graph</h2>
//           <img src={graphUrl} alt="Temperature vs RPM" style={{ width: "100%" }} />
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;





// App.js
// import React, { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [numRpms, setNumRpms] = useState(1);
//   const [rpmList, setRpmList] = useState([""]);
//   const [velocityX, setVelocityX] = useState("");
//   const [velocityY, setVelocityY] = useState("");
//   const [velocityZ, setVelocityZ] = useState("");
//   const [results, setResults] = useState([]);
//   const [loading, setLoading] = useState(false);

//   const handleNumRpmsChange = e => {
//     const n = parseInt(e.target.value, 10) || 0;
//     setNumRpms(n);
//     setRpmList(Array(n).fill(""));
//   };

//   const handleRpmChange = index => e => {
//     const list = [...rpmList];
//     list[index] = e.target.value;
//     setRpmList(list);
//   };

//   const runSimulation = async () => {
//     setLoading(true);
//     try {
//       const payload = {
//         rpms: rpmList.map(Number),
//         velocityX: parseFloat(velocityX),
//         velocityY: parseFloat(velocityY),
//         velocityZ: parseFloat(velocityZ)
//       };
//       const { data } = await axios.post("http://localhost:5000/run_simulation", payload);
//       if (Array.isArray(data.results)) setResults(data.results);
//     } catch (err) {
//       console.error(err);
//       alert("Simulation failed. Check console.");
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="container">
//       <h1>ANSYS Simulation</h1>

//       <div className="section">
//         <h2>How many RPM values?</h2>
//         <input
//           type="number"
//           min="1"
//           value={numRpms}
//           onChange={handleNumRpmsChange}
//         />
//       </div>

//       <div className="section parameters">
//         {rpmList.map((val, idx) => (
//           <div key={idx} className="parameter-box">
//             <h3>{`RPM ${idx + 1}`}</h3>
//             <input
//               type="number"
//               value={val}
//               onChange={handleRpmChange(idx)}
//             />
//           </div>
//         ))}
//       </div>

//       <div className="section">
//         <h2>Translational Velocity (m/s)</h2>
//         <div className="parameters">
//           {['X','Y','Z'].map(axis => (
//             <div key={axis} className="parameter-box">
//               <label>{axis}:</label>
//               <input
//                 type="number"
//                 value={{X:velocityX, Y:velocityY, Z:velocityZ}[axis]}
//                 onChange={e => {
//                   const v = e.target.value;
//                   if (axis === 'X') setVelocityX(v);
//                   if (axis === 'Y') setVelocityY(v);
//                   if (axis === 'Z') setVelocityZ(v);
//                 }}
//               />
//             </div>
//           ))}
//         </div>
//       </div>

//       <button
//         className="run-button"
//         onClick={runSimulation}
//         disabled={loading}
//       >
//         {loading ? "Running Simulation..." : "Run Simulation"}
//       </button>

//       {/* Results Display */}
//       {results.length > 0 && (
//         <div className="section results-container">
//           <h2>Results</h2>
//           {results.map((res, idx) => {
//             const { rpm, temperature_result, contour_file } = res;
//             return (
//               <div key={idx} className="result-box">
//                 <strong>RPM:</strong> {rpm} &nbsp;|&nbsp; 
//                 <strong>Avg Temp:</strong> {temperature_result.toFixed(2)}
//                 {contour_file && (
//                   <div className="contour-image" style={{ marginTop: '10px' }}>
//                     <img
//                       src={contour_file}
//                       alt={`Contour for RPM ${rpm}`}
//                       style={{ width: '100%', maxWidth: '400px' }}
//                     />
//                   </div>
//                 )}
//               </div>
//             );
//           })}
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;

