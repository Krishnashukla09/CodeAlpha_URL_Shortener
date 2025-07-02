# 🔗 URL Shortener

A fast and lightweight URL shortening application built with Python Flask. It allows users to convert long, ugly URLs into clean, short, shareable links.

---

## 🚀 Features

- 📥 Enter any long URL and get a short one instantly
- 🔗 Automatically redirects short URL to original destination
- 📊 Optional visit counter to track number of clicks
- 💾 Stores all links in MySQL database
- 🧹 Admin access to view all shortened URLs

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS (Bootstrap)
- **Backend:** Python (Flask)
- **Database:** MySQL
- **Tools:** Git, VS Code, Postman

---

## 📂 Folder Structure
```bash
url-shortener/
├── app.py
├── templates/
│ ├── index.html
│ └── result.html
├── static/
│ └── styles.css (if any)
├── db_config.sql
└── README.md

---




## 💻 How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/Krishnashukla09/url-shortener.git
cd url-shortener

2. Install required packages:
```bash
pip install flask

3. Set up MySQL database:
```bash
Use the provided db_config.sql file

Update DB credentials in app.py

4. Run the Flask server:
```bash
python app.py

5.Open your browser and navigate to:
```bash
http://localhost:5000

