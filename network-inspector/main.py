from fastapi import FastAPI, UploadFile, File
from network_analyzer import analyze_network

app = FastAPI(title="NetworkInspector")
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
async def scan_network(file: UploadFile = File(...)):
    return analyze_network(file)
