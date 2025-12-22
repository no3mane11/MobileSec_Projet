from fastapi import FastAPI, UploadFile, File
from ci_runner import run_ci_scan
from fastapi.middleware.cors import CORSMiddleware

# ... après l'instanciation de app = FastAPI() ...



app = FastAPI(title="CIConnector")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Autorise ton frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run-ci-scan")
async def run_scan(file: UploadFile = File(...)):
    # On passe directement l'objet file au runner
    return run_ci_scan(file)
