# 📄 Automated Resume Parser

A full-stack resume parsing application built with **Python, FastAPI, PyMuPDF, python-docx, HTML, CSS, and JavaScript**.

Upload a PDF or DOCX resume and extract structured information such as contact details, skills, education, experience, LinkedIn, and GitHub links.

## ✨ Features
- PDF and DOCX resume parsing
- Name, email and phone extraction
- Skills detection
- Education and experience extraction
- LinkedIn/GitHub extraction
- Interactive web interface
- FastAPI Swagger documentation
- Automated API tests
- Render-ready deployment

## 🛠️ Tech Stack
Python • FastAPI • PyMuPDF • python-docx • Regex • HTML/CSS/JavaScript • Pytest • Render

## 🚀 Run Locally
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Open `http://127.0.0.1:8000`

Swagger: `http://127.0.0.1:8000/docs`

## 🧪 Tests
```bash
python -m pytest
```

## 🔮 Future Improvements
- NLP-based entity extraction
- Resume scoring
- Job-description matching
- Skill gap analysis
- Database storage
- Authentication
- Resume analytics dashboard
- LLM-assisted extraction
