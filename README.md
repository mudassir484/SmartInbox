
# 📬 SmartInbox— Smart Email Platform with LLaMA-Powered Tone & Spam Detection

MailSense is a modern, secure, and intelligent email web application that allows users to send, receive, and analyze emails. Built with **Flask**, **SQLite**, and integrated with **LLaMA 3.2 3B GGUF** models for local **tone classification** and **spam detection**, it provides real-time NLP capabilities directly in your inbox.

## ✨ Features

- 📨 Send and receive emails between users
- 🧠 AI-powered tone classification (polite, formal, neutral, urgent)
- 🚫 Spam detection using LLaMA local inference
- 📊 Admin dashboard with analytics and email monitoring
- 📬 Inbox & Sent views with read tracking
- 🧾 Lightweight SQLite database
- 🔐 Secure login/register flow with password hashing
- 🎨 Responsive Bootstrap UI with aesthetic polish

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mudassir484/SmartInbox

````

### 2. Set Up the Virtual Environment

```bash
python -m venv .venv
.venv/Scripts/activate  # On Windows
# Or use: source .venv/bin/activate  # On Mac/Linux
pip install -r backend/requirements.txt
```

### 3. Download the LLaMA Model (Offline Inference)

> ✅ Recommended Model: [Llama-3.2-3B-Instruct-GGUF](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF)

* Download the file:
  **`llama-3.2-3b-instruct-q4_k_m.gguf`**

* Place it inside the project at:
  `Email/models/llama-3.2-3b-instruct-q4_k_m.gguf`

> 💡 The app uses [`llama-cpp-python`](https://github.com/abetlen/llama-cpp-python) to load and run the model **entirely offline**, no OpenAI API keys needed.

---

### 4. Run the Application

```bash
python app.py
```

The app will start on [http://localhost:5000](http://localhost:5000) by default.

---

## 🧪 Tech Stack

| Layer         | Tech Used                         |
| ------------- | --------------------------------- |
| Backend       | Python, Flask, SQLite             |
| AI/NLP        | LLaMA 3.2 3B (GGUF via llama-cpp) |
| Frontend      | HTML, CSS, Bootstrap 5            |
| Auth/Security | Flask Sessions, Bcrypt            |
| Deployment    | Local (production-ready layout)   |

---

## 🛠️ Folder Structure

```
Email/
├── app.py                  # Main Flask App
├── backend/
│   ├── llama_utils.py      # Model integration utilities
│   ├── requirements.txt    # All dependencies
├── templates/              # HTML templates
├── static/                 # CSS, JS, Icons
├── models/                 # GGUF LLaMA model goes here
└── mailsense.db            # SQLite DB (auto-created)
```

---

## 📸 Screenshots

>
> * Login
> * Register
> * Sender dashboard
> * Inbox with tone and spam tags
> * Admin panel

---

---

## 🧠 Future Improvements

* ✉️ Email scheduling and drafts
* 📎 File attachments support
* 🌍 Dockerized deployment
* 📈 Model upgrade to LLaMA 3.2 8B with quantization

---                   
