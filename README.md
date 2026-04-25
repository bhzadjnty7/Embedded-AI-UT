

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=Embedded%20AI%20Systems%20Projects&fontSize=35&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>
</p>

# 🧠 Embedded AI Systems Projects

![Language](https://img.shields.io/badge/Language-Python%20%7C%20Verilog-blue)
![Domain](https://img.shields.io/badge/Domain-Embedded%20AI-green)
![Architecture](https://img.shields.io/badge/Focus-LNS%20%7C%20RNS%20%7C%20MAC-orange)
![Simulation](https://img.shields.io/badge/Simulator-ModelSim-purple)
![Status](https://img.shields.io/badge/Status-Complete-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview

This repository contains a set of course assignments developed for the **Embedded AI Systems** course at the **University of Tehran (Faculty of Electrical & Computer Engineering)**.

The projects focus on **efficient numerical representations and hardware-aware computation techniques** that are essential in modern embedded AI systems, especially under constraints such as limited power, memory, and computational resources.

The work covers both **software-level modeling (Python)** and **hardware-level design (Verilog)**, providing a complete perspective from algorithmic analysis to digital implementation.

---

## 🏫 Course Information

* **Course:** Embedded AI Systems
* **University:** University of Tehran
* **Faculty:** Electrical & Computer Engineering
* **Instructors:** Dr. Mehdi Modarresi, Dr. Mostafa Salehi

---

## 📂 Repository Structure

```bash
Embedded-AI-Systems-Projects/
│
├── CA1_LNS/
│   ├── Report.pdf
│   ├── Notebook.ipynb
│   ├── Source Codes
│
├── CA2_RNS/
│   ├── Report.pdf
│   ├── Notebook.ipynb
│   ├── Source Codes
│
├── CA3_RNS_MAC_Verilog/
│   ├── Report.pdf
│   ├── Verilog Files
│   ├── Testbench
│
└── README.md
```

---

## 🧮 CA1 – Logarithmic Number System (LNS)

### 📖 Description

Implementation and evaluation of the **Logarithmic Number System (LNS)** as an alternative to floating-point arithmetic for embedded systems.

### ⚙️ Key Features

* Real ↔ LNS conversion
* Fixed-point logarithmic representation
* Quantization and approximation analysis
* Dynamic range evaluation
* Trade-off analysis across parameters (base, bit-width, precision)

### 🎯 Insight

LNS transforms multiplication/division into addition/subtraction, making it highly suitable for **resource-constrained hardware**.

---

## 🧮 CA2 – Residue Number System (RNS)

### 📖 Description

Exploration of the **Residue Number System (RNS)** for parallel and carry-free arithmetic.

### ⚙️ Key Features

* Forward conversion (Integer → RNS)
* Reverse conversion using:

  * Chinese Remainder Theorem (CRT)
  * Garner’s Algorithm (MRC)
* Signed & unsigned representations
* Arithmetic operations in RNS domain

### 🚀 Insight

RNS enables **fully parallel computations** and eliminates carry propagation, making it ideal for **high-speed embedded AI hardware**.

---

## 🧠 CA3 – RNS-based MAC Unit (Verilog)

### 📖 Description

Hardware design of a **Multiply-Accumulate (MAC)** unit using **RNS arithmetic**, implemented in Verilog and simulated in ModelSim.

### ⚙️ Architecture

* FSM-based Controller
* Modular Datapath design
* RNS arithmetic units (Adder, Multiplier, Converters)

### 📊 Features

* Parallel arithmetic execution
* Comparison with binary implementation
* Area and delay analysis

---

## ▶️ How to Run CA3 (ModelSim Simulation)

1. Create a new project in ModelSim
2. Add all Verilog files (`.v`)
3. Compile all modules
4. Run the testbench (`MAC_TB.v`)
5. Observe:

   * Waveforms
   * Transcript output

✔ The simulation validates correctness of the MAC computation.

---

## 🎯 Key Takeaways

* Efficient number systems are critical in Embedded AI
* LNS → simplifies multiplication
* RNS → enables parallelism
* Hardware/software co-design improves performance

---

## 🛠 Technologies Used

* Python (NumPy, analysis)
* Verilog HDL
* ModelSim

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Behzad Jannati**
M.Sc. Student – Computer Architecture
University of Tehran

---

## ⭐️ Support

If you find this repository useful, consider giving it a ⭐️

