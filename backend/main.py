from pathlib import Path
import re, shutil, uuid
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from backend.parser import parse_resume

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
FRONTEND_DIR = BASE_DIR / "frontend"
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI(title="Automated Resume Parser", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])

@app.get("/health")
def health():
    return {"status": "healthy", "service": "automated-resume-parser"}

@app.post("/api/parse")
async def parse_resume_api(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(400, "No file selected.")
    ext = Path(file.filename).suffix.lower()
    if ext not in {".pdf", ".docx"}:
        raise HTTPException(400, "Only PDF and DOCX files are supported.")
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", file.filename)
    path = UPLOAD_DIR / f"{uuid.uuid4().hex}_{safe}"
    with path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        result = parse_resume(path)
        result["filename"] = file.filename
        return result
    finally:
        path.unlink(missing_ok=True)

@app.get("/")
def frontend():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/{asset:path}")
def static_assets(asset: str):
    requested = FRONTEND_DIR / asset
    if requested.is_file():
        return FileResponse(requested)
    return FileResponse(FRONTEND_DIR / "index.html")
