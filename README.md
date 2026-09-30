# 📄 Automated Resume Parser

A full-stack **Automated Resume Parser** that extracts structured information from PDF and DOCX resumes. The application supports both normal text-based PDFs and scanned/image-based PDFs using **Tesseract OCR**.

🌐 **Live Demo:** https://automated-resume-parser-ld4g.onrender.com

## ✨ Features

- 📄 PDF and DOCX resume upload
- 🔎 Text extraction from normal PDFs using PyMuPDF
- 🖼️ OCR extraction from scanned/image-based PDFs using Tesseract
- 👤 Name extraction
- 📧 Email extraction
- 📱 Phone number extraction
- 🔗 LinkedIn and GitHub link detection
- 🛠️ Skill keyword detection
- 🎓 Education section extraction
- 💼 Experience section extraction
- 🌐 Interactive web interface
- 📚 FastAPI Swagger API documentation
- 🧪 Automated API tests
- 🐳 Docker-based deployment
- 🚀 Live deployment on Render

## 🏗️ Architecture

```text
                    Resume (PDF / DOCX)
                            │
                            ▼
                    FastAPI Backend
                            │
             ┌──────────────┴──────────────┐
             │                             │
       Text-based PDF                 Scanned PDF
             │                             │
         PyMuPDF                    Tesseract OCR
             │                             │
             └──────────────┬──────────────┘
                            │
                            ▼
                    Resume Text Extraction
                            │
                            ▼
                 Structured Information
                            │
          ┌─────────┬───────┼────────┬─────────┐
          ▼         ▼       ▼        ▼         ▼
        Name      Email   Phone    Skills   Education
                            │
                            ▼
                       Experience
                            │
                            ▼
                     Web Interface
```

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Backend | Python, FastAPI |
| PDF Parsing | PyMuPDF |
| OCR | Tesseract OCR, pytesseract |
| DOCX Parsing | python-docx |
| Text Processing | Python Regex |
| Frontend | HTML, CSS, JavaScript |
| Testing | Pytest, HTTPX |
| Containerization | Docker |
| Deployment | Render |
| Version Control | Git, GitHub |

## 📁 Project Structure

```text
Automated-Resume-Parser/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   └── parser.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── tests/
│   └── test_api.py
├── uploads/
│   └── .gitkeep
├── Dockerfile
├── requirements.txt
├── render.yaml
├── .python-version
├── .gitignore
└── README.md
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/urs-raju-0302/Automated-Resume-Parser.git
cd Automated-Resume-Parser
```

### 2. Create and activate virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Python dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Install Tesseract OCR

For scanned PDF support on Windows, install Tesseract OCR and make sure it is available at:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

### 5. Start the application

```powershell
uvicorn backend.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

## 🐳 Docker

The production deployment uses Docker so that the application can include the Tesseract OCR system package together with the Python environment.

Build:

```bash
docker build -t automated-resume-parser .
```

Run:

```bash
docker run -p 8000:8000 automated-resume-parser
```

## 🔌 API

### Health Check

```http
GET /health
```

### Parse Resume

```http
POST /api/parse
```

Accepts:

- `.pdf`
- `.docx`

Returns structured JSON containing extracted resume information.

## 🧪 Tests

Run:

```bash
python -m pytest
```

The test suite covers the API health endpoint and invalid file-type validation.

## 🚀 Deployment

The application is deployed using **Docker + Render**.

Production flow:

```text
GitHub → Render → Docker → FastAPI + Tesseract OCR
```

### Live Application

https://automated-resume-parser-ld4g.onrender.com

## 🎯 Project Objective

The objective of this project is to automate the initial extraction of important information from resumes and convert unstructured resume documents into structured data that can be used by recruitment and career-readiness systems.

## 🔮 Future Improvements

- NLP-based named entity recognition
- Improved LinkedIn/GitHub detection
- More robust skill extraction
- Resume scoring
- Job-description matching
- Skill-gap analysis
- Database storage
- Authentication and user accounts
- Resume analytics dashboard
- LLM-assisted extraction
- Support for additional document formats

## 👨‍💻 Author

**Poshamolla Raju**

GitHub: https://github.com/urs-raju-0302
