import React from "react";
import topView1 from "../assets/top3000.png";
import frontView1 from "../assets/front3000.png";
import sideView1 from "../assets/side3000.png";
import topView2 from "../assets/top4000.png";
import frontView2 from "../assets/front4000.png";
import sideView2 from "../assets/side4000.png";
import topView3 from "../assets/top5000.png";
import frontView3 from "../assets/front5000.png";
import sideView3 from "../assets/side5000.png";
import topView4 from "../assets/top6000.png";
import frontView4 from "../assets/front6000.png";
import sideView4 from "../assets/side6000.png";
import topView5 from "../assets/top7000.png";
import frontView5 from "../assets/front7000.png";
import sideView5 from "../assets/side7000.png";
import "./ContourPlots.css";

function ContourPlots() {
  const rpmSets = [
    { rpm: 3000, images: [topView1, frontView1, sideView1] },
    { rpm: 4000, images: [topView2, frontView2, sideView2] },
    { rpm: 5000, images: [topView3, frontView3, sideView3] },
    { rpm: 6000, images: [topView4, frontView4, sideView4] },
    { rpm: 7000, images: [topView5, frontView5, sideView5] },
  ];

  return (
    <div className="contour-page">
      {rpmSets.map((set, idx) => (
        <div key={idx}>
          <h1 className="contour-heading">Contour Plots for {set.rpm} RPM</h1>
          <div className="contour-images">
            {set.images.map((src, i) => (
              <div
                key={i}
                className="contour-card"
                style={{ cursor: 'pointer' }}
                onClick={() => window.open(src, '_blank')}
              >
                <img
                  src={src}
                  alt={`View ${i + 1}`}
                  onMouseEnter={e => e.currentTarget.style.transform = 'scale(1.05)'}
                  onMouseLeave={e => e.currentTarget.style.transform = 'scale(1)'}
                />
                <p>{['Top view', 'Front view', 'Side view'][i]}</p>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

export default ContourPlots;
