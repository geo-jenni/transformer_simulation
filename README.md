
# 🔧 Transformer Replacement Simulation

This Streamlit web app simulates the safe and correct procedure for replacing a utility transformer on a distribution pole. It is designed for training, safety evaluation, and procedural reinforcement for utility line workers.

## 🚀 Features

- ✅ Interactive 10-stage simulation
- ✅ Decision-tree logic with immediate feedback
- ✅ Scoring system with pass/fail thresholds
- ✅ Downloadable action log
- ✅ Web deployment on Streamlit Cloud

---

## 🧱 Project Structure

```
transformer_simulation/
├── simulation.py                        # Main Streamlit app
├── transformer_simulation_logic_tree.json  # Decision tree logic
├── requirements.txt                    # Dependencies
└── README.md                           # Project documentation
```

---

## 📦 Requirements

- Python 3.7+
- Streamlit
- Pandas

Install using:

```bash
pip install -r requirements.txt
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **“New App”**
4. Set the app file to `simulation.py`
5. Deploy and share your link!

---

## 🎯 Simulation Stages

1. PPE & Job Briefing
2. Hazard Identification
3. System Isolation
4. Voltage Verification
5. Grounding Setup
6. Disconnect Transformer
7. Remove Old Unit
8. Install New Transformer
9. Reconnect & Test
10. Power-Up & Final Inspection

---

## 🎓 Scoring System

| Action Type      | Score |
|------------------|-------|
| Correct Action   | +10   |
| Unsafe Action    | -10 to -20 |
| Critical Mistake | -30   |

**Passing Score:** 70+

---

## 📄 License

This project is for educational and professional training use. Not for commercial distribution without permission.

---

## 👷 Author

Created with ❤️ by [ScholarGPT] — transforming simulation-based training.
