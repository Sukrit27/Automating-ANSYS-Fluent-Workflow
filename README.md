# 🔌 Live Simulation of a 3-Phase AC Motor in ANSYS Fluent

This project provides a **web-based interface** for live thermal simulation of a **3-phase AC motor**, powered by **ANSYS Fluent** and **Maxwell** integration. The system simulates temperature profiles dynamically based on varying **RPM** and **Power input**, visualizing **ohmic losses** and **temperature contours** in real time for efficient analysis.

![WhatsApp Image 2025-05-14 at 22 02 51_b7b01868](https://github.com/user-attachments/assets/beb1ca94-187c-4621-9e8a-d8fd6410ad53)

![Website Homepage](images/homepage.png)

---

## 🛠️ Key Features

- 🌐 **Interactive Web Frontend**  
  Users can input a range of RPM and power values for live simulations.

- 🔄 **Backend Integration with PyFluent**  
  Uses `pyfluent` and Python to communicate with **ANSYS Fluent**.

- ⚡ **Ohmic Losses from ANSYS Maxwell**  
  Simulated ohmic losses are imported from Maxwell and used as thermal input.

- 🌡️ **Live Temperature Contour Visualization**  
  Each simulation returns temperature data along with **temperature contours**.

- 📊 **Results Visualization**  
  Simulation outputs are displayed clearly in the frontend for comparative analysis.

---

## 📸 Screenshots

### 🧮 Input Form for RPM & Power
![Input Form](images/input-form.png)

---

### 📈 Simulation Results Display
![Results Table](images/results-display.png)

---

### 🌡️ Temperature Contour Example
![Temperature Contour](images/temp-contour.png)

---

## 🔧 Tech Stack

| Layer        | Technologies Used                          |
|--------------|---------------------------------------------|
| Frontend     | HTML, CSS, JavaScript, React (optional)     |
| Backend      | Python, Flask / FastAPI                     |
| Simulation   | ANSYS Fluent + pyFluent, ANSYS Maxwell      |
| Data Handling| Stored locally                              |
| Visualization| Matplotlib                                  |

---

## 🚀 How It Works

1. **User Input:**  
   RPM and Power values are entered via the frontend.

2. **Backend Processing:**  
   These values are sent to the backend where `pyfluent` interfaces with Fluent.

3. **Thermal Simulation:**  
   Fluent uses ohmic loss data from Maxwell to simulate heat generation.

4. **Output Rendering:**  
   Temperatures and heat contours are sent back to the frontend and displayed dynamically.

---

## 🖼️ 3D Contour Generation

Temperature contours are generated using ANSYS Fluent’s post-processing tools and can be exported as:
- PNG / JPEG images

---

## 🏁 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/Sukrit27/Automating-ANSYS-Fluent-Workflow.git
   cd backend
   python server.py

   **In another terminal**
   npm i
   npm start
