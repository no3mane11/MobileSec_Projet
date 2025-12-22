from fastapi import FastAPI
from report_builder import build_report

app = FastAPI(title="ReportGen")
from fastapi.middleware.cors import CORSMiddleware

# ... après l'instanciation de app = FastAPI() ...

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Autorise ton frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-report")
async def generate_report(data: dict):
    return build_report(data)
