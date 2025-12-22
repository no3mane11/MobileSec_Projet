from fastapi import FastAPI, UploadFile, File
from scanner import analyze_apk

app = FastAPI(title="APKScanner")
from fastapi.middleware.cors import CORSMiddleware

# ... après l'instanciation de app = FastAPI() ...

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Autorise ton frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/scan")
async def scan_apk(file: UploadFile = File(...)):
    result = analyze_apk(file)
    return result
