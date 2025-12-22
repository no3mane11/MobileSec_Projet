from fastapi import FastAPI, UploadFile, File
from crypto_analyzer import analyze_crypto

app = FastAPI(title="CryptoCheck")
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
async def scan_crypto(file: UploadFile = File(...)):
    return analyze_crypto(file)
