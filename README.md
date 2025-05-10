# 🐞 Bug Hunter’s Toolkit

**Bug Hunter’s Toolkit** is a simulated cybersecurity environment built with Django to demonstrate core penetration testing techniques in a safe and ethical way.

This toolkit does **not** perform any real security scans or attacks. Instead, it mimics tools like `nmap`, brute-force logic, and HTTP header inspection to showcase your backend development and security knowledge in a production-ready interface.

---

## 🧩 Features

- 🔎 **Nmap Port Scan Simulation**  
  Simulated terminal output mimicking `nmap` port scanning behavior.

- 📥 **HTTP Header Analysis**  
  Inspects and prints HTTP response headers from a real external site.

- 🔐 **Brute Force Simulation**  
  Simulates a dictionary-based brute-force attack with fake credentials.

- 📁 **Download Reports**  
  Export each simulation’s result as a `.txt` file for demonstration.

- ✅ **Educational Disclaimer & Best Practices**  
  Includes a footer notice and security tips to reinforce ethical usage.

---

## 🚀 Tech Stack

- **Framework:** Django
- **Language:** Python 3.13+
- **Deployment:** Railway.app
- **Additional Tools:** Gunicorn, Requests, Python-Nmap

---

## 📸 Live Demo

▶️ https://bughunterstoolkit-production.up.railway.app

---

## 📂 Local Installation

```bash
git clone https://github.com/your-username/bug-hunters-toolkit.git
cd bug-hunters-toolkit
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py runserver

📜 License
This project is licensed under the MIT License.

⚠️ Disclaimer
This toolkit is a simulated environment intended purely for educational and demonstrational purposes.
It does not perform any real security scans or attacks.

💬 Author
Developed by Half-Half Man,
Synthesis of Code and Water.

🔗 Portfolio Website - TBA
📧 nmihajlovic.dev@gmail.com
