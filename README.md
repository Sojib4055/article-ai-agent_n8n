
# 📘 AI Article Agent — Complete Project Documentation

This project is an **AI-powered Article Processing System** that extracts summaries and insights from any article URL using:

Lovable app link :    https://mail-gist.lovable.app/

Video Link :   https://drive.google.com/file/d/1VTm4McjJee4zTJHEyZlgtv02s1sdUOlD/view?usp=sharing


- **FastAPI backend (Python)**
- **n8n automation workflow**
- **Claude AI (Anthropic) for summarization & insights**
- **Google Sheets logging**
- **Automated email delivery**

---

# 🚀 Features

### 🔹 FastAPI Backend
- Receives *email* and *article URL*
- Validates inputs
- Generates unique `session_id`
- Forwards data to n8n webhook
- Returns immediate status response

### 🔹 n8n Workflow
- Scrapes article HTML
- Summarizes using Claude
- Extracts insights using Claude
- Logs data to Google Sheets
- Sends formatted results via Gmail

### 🔹 Fully Automated Pipeline
Send → Process → Summarize → Log → Email  
No manual steps required.

---

# 📂 Project Structure

```
/project
│── main.py                # FastAPI backend
│── .env                   # Environment variables
│── requirements.txt       # Dependencies
│── My workflow.json       # n8n workflow
│── README.md              # Documentation
```

---

# 🛠️ Installation

### 1️⃣ Clone the Repository

```bash
git clone <YOUR_GIT_URL>
cd <YOUR_PROJECT_NAME>
```

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

Required libraries:
- fastapi  
- uvicorn  
- httpx  
- python-dotenv  
- email-validator  

---

# 🔧 Environment Variables

Create a `.env` file:

```
N8N_WEBHOOK_URL=https://sojib4055.app.n8n.cloud/webhook/article-ai-agent
```

---

# ▶️ Running the FastAPI Backend

```bash
uvicorn main:app --reload
```

API docs available at:

```
http://127.0.0.1:8000/docs
```

---

# 📬 API Usage

### POST `/process-article`

#### Request Body
```json
{
  "email": "example@gmail.com",
  "article_url": "https://example.com"
}
```

#### Response
```json
{
  "session_id": "uuid-generated",
  "status": "processing",
  "n8n_status_code": 200,
  "n8n_response": { ... }
}
```

---

# 🤖 n8n Workflow Breakdown

### 1️⃣ Webhook Trigger
Receives email, article URL, session_id.

### 2️⃣ Extract Webhook Data Node
Prepares structured JSON.

### 3️⃣ Article Scraper Node
Uses **HTTP Request** with browser-like User-Agent.

### 4️⃣ Summary (Claude)
Prompt:
```
Summarize the article in 3–5 sentences...
```

### 5️⃣ Insights (Claude)
Prompt:
```
Extract 3–5 key insights...
```

### 6️⃣ Merge Summary & Insights Node
Combines model outputs.

### 7️⃣ Google Sheets Logging
Stores:
- email  
- article_url  
- summary  
- insights  
- timestamp  

### 8️⃣ Gmail Node
Sends a fully formatted HTML email.

---

# 📡 Testing

### With cURL:
```bash
curl -X POST http://127.0.0.1:8000/process-article      -H "Content-Type: application/json"      -d '{"email":"test@gmail.com","article_url":"https://example.com"}'
```

---

# 🌐 Deployment

### Backend Can Be Deployed on:
- Render
- Railway
- Vercel (ASGI)
- DigitalOcean
- AWS EC2

### n8n Already Hosted At:
```
https://sojib4055.app.n8n.cloud/
```

---

# 🛠️ Troubleshooting

### ❗ Article Scraper URL Undefined
Ensure:
```
url:={{ $json.article_url }}
```
is correctly passed from Webhook → Set → Scraper.

---

# 📄 License
Private project — personal use only unless permitted.

---

# 🎉 You're All Set!
If you want:
- PDF version  
- DOCX version  
- GitHub badges  
- More diagrams or visuals  
Just tell me!
