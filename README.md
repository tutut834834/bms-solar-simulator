![image](https://github.com/user-attachments/assets/4e4cf1dc-3080-463f-8bd1-ab066cbfd137)
# 🔋 BMS Solar Simulator ☀️

A modular, real-time simulation of a **Battery Management System (BMS)** integrated with **solar generation**, **inverter logic**, and **motor load control** — perfect for educational demos, prototyping, and testing energy systems.

---

## 🧠 Features

- ⚡ Simulated **solar panel behavior** with:
  - Dynamic **cloud cover**
  - Simulated **dirt accumulation**
- 🔋 **Battery behavior** with:
  - State of charge (SOC)
  - Imbalance simulation
- 🔌 **Inverter control** with output monitoring
- 🌀 **Motor load** response modeling
- 📊 Real-time **data plotting** using `matplotlib`
- 💾 Modular Python design (easy to extend)

---

## 📁 File Structure

```
BMS/
├── BMS.py               # Main simulation script
├── battery.py           # Battery logic and status
├── controller.py        # System controller logic
├── inverter.py          # Inverter behavior
├── motor.py             # Motor load simulation
├── solar.py             # Solar generation + environmental factors
├── atrix.bms.log        # Log file output
└── __pycache__/         # Cached compiled Python files
```

---

## 🚀 Quick Start

1. **Clone the repository**

```bash
git clone git@github.com:tutut834834/bms-solar-simulator.git
cd bms-solar-simulator
```

2. **Install dependencies**

```bash
pip install matplotlib
```

3. **Run the simulator**

```bash
python BMS.py
```

---

## 📈 Example Output

The simulation will:
- Plot battery voltage, SOC, solar output, inverter output, and motor load
- Simulate over 10,000 cycles in real-time
- Log key outputs and system statuses to `atrix.bms.log`

---

## 🛠 Customize It!

Want to tweak the physics or logic?

- Add your own `solar_fluctuation.py` and import into `solar.py`
- Modify thresholds or feedback logic in `controller.py`
- Hook into MQTT or CAN bus for real-world prototyping

---

## 🧪 Planned Enhancements

- 🔄 Data export to CSV
- 🌐 Web-based dashboard (Flask or Streamlit)
- 🔌 Integration with real sensor data
- 🧠 Machine learning-based smart controller

---

## 👨‍💻 Author

**tutut834834**  
> Developed with passion, purpose, and some occasional coffee ☕  
> Powered by solar inspiration ☀️

---

## 📝 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
