# 📬 SmartInbox — AI‑Powered Smart Email Platform

SmartInbox is a **modern, secure, and intelligent email web application** that allows you to send, receive, and analyze both **internal** and **external** emails.  
It features **AI‑powered tone detection, spam detection, summarization, and read receipts** — all inside a clean, modern web interface.

Built with **Flask**, **SQLite**, and integrated with **LLaMA 3.2 (GGUF)** models for **offline AI inference**, SmartInbox delivers real‑time NLP insights without relying on third‑party AI APIs.

---

## ✨ Key Features

### 📤 Email Sending & Receiving
- **Internal email** between SmartInbox users.
- **External email** sending via Gmail SMTP.
- **Reply directly** from inbox with pre‑filled details.
- **Tracking pixel** for external emails — detect when Gmail recipients open your message.

### 🧠 AI‑Powered Intelligence
- **Tone classification** — friendly, formal, urgent, angry, sarcastic, etc.
- **Spam detection** — powered by local LLaMA inference.
- **AI summarization** of long emails — quick previews without reading the whole message.

### 📊 Tracking & Analytics
- **Internal read receipts** — automatically marks email as read when opened in the app.
- **External Gmail tracking pixel** — detects when recipient views your message.
- **Sender dashboard** — view all internal & external sent emails in one place.
- **Admin analytics dashboard**:
  - Active users
  - Total emails sent
  - Spam count
  - Read statistics

### 🔐 Security & User Management
- Secure **login/register** with password hashing (**bcrypt**).
- Admin control panel — view all emails and users.
- Spam flagging in UI for quick identification.

### 🎨 Modern UI
- Responsive **Bootstrap 5** design.
- Inbox cards with **tone badges** & **spam labels**.
- Sent dashboard and admin panel with charts and tables.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

git clone https://github.com/mudassir484/SmartInbox
cd SmartInbox
2️⃣ Set Up the Virtual Environment
python -m venv .venv
.venv/Scripts/activate  # Windows
# OR
source .venv/bin/activate  # Mac/Linux

pip install -r backend/requirements.txt
3️⃣ Download & Place the LLaMA Model
Recommended Model: Llama-3.2-3B-Instruct-GGUF


Edit
llama-3.2-3b-instruct-q4_k_m.gguf
Place in:

Copy
Edit
Email/models/llama-3.2-3b-instruct-q4_k_m.gguf
💡 Uses llama-cpp-python for offline AI inference.

4️⃣ Configure Environment Variables
Create a .env file:

Edit
SENDER_EMAIL=yourappemail@gmail.com
EMAIL_PASS=your_gmail_app_password
⚠️ Use a Gmail App Password — not your personal password.

5️⃣ Run the App
Copy
Edit
python app.py
Open in your browser:
http://localhost:5000

📡 How External Read Tracking Works
SmartInbox embeds a tiny tracking pixel image in external Gmail emails:


<img src="https://your-domain.com/open_tracker/<email_id>.png" width="1" height="1" />
When the recipient opens the email in Gmail:

Gmail loads the tracking image.

SmartInbox records the open time in the database.

You can view this in your Sent Dashboard and Admin Panel.

📌 Note: Gmail caches images — so first open is always tracked, but repeated opens may not trigger new logs.

🧪 Tech Stack
Layer	Tech Used
Backend	Python, Flask, SQLite
AI/NLP	LLaMA 3.2 3B (GGUF via llama-cpp)
Frontend	HTML, CSS, Bootstrap 5
Auth/Security	Flask Sessions, bcrypt password hashing
Email Sending	Gmail SMTP + Internal routing
Tracking	DB read receipts + tracking pixel
Deployment	Local / production‑ready Flask app

📂 Folder Structure
bash
Copy
Edit
Email/
├── app.py                  # Main Flask app
├── backend/
│   ├── llama_utils.py      # AI tone/spam/summarizer
│   ├── requirements.txt    # Dependencies
├── templates/              # HTML templates (Inbox, Admin, Login, etc.)
├── static/                 # CSS, JS, Icons
├── models/                 # LLaMA model (.gguf)
├── Sbox.db                 # SQLite DB (auto-created)
└── .env                    # Email credentials
📸 UI Overview
Login & Register

Sender Dashboard — internal + external sent emails

Inbox — read/unread states, tone & spam labels, quick view

Email Modal — full message view, summarization, reply

Admin Panel — charts, stats, user & email management

🔮 Future Roadmap
📅 Email scheduling & drafts

📎 File attachments

🗂 Folders & labels

🐳 Dockerized deployment

⚡ Upgrade to LLaMA 3.2‑8B with quantization
