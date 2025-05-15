# 🔌 Live Simulation of a 3-Phase AC Motor in ANSYS Fluent

This project provides a **web-based interface** for real-time thermal simulation of any physical model in **ANSYS Fluent**, using external loss data from tools like **ANSYS Maxwell**. While this implementation uses a **3-phase AC motor** as an example, the system is **fully adaptable to other models**—making it a flexible framework for multiphysics simulation and analysis.


![WhatsApp Image 2025-05-14 at 22 02 51_b7b01868](https://github.com/user-attachments/assets/beb1ca94-187c-4621-9e8a-d8fd6410ad53)


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

  - 🧩 **Model-Agnostic Design**  
  This system can be configured for **any geometry or physics model**, not just motors.

- 📊 **Results Visualization**  
  Simulation outputs are displayed clearly in the frontend for comparative analysis.

---

## 📸 Screenshots

### 🧮 Input Form for RPM & Power
![WhatsApp Image 2025-05-14 at 22 04 46_6fea8ae9](https://github.com/user-attachments/assets/f2496138-0b52-4ec9-98fb-7a61e55d56c0)


---

### 📈 Simulation Results Display
![WhatsApp Image 2025-05-14 at 21 26 59_9578d522](https://github.com/user-attachments/assets/d20d643d-0e02-4dd0-a9e9-520380bebf87)


---

### 🌡️ Temperature Contour Example
![WhatsApp Image 2025-05-14 at 22 05 15_4f1f1d82](https://github.com/user-attachments/assets/c50e135e-385e-41da-850a-eb180b82a5b7)


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
