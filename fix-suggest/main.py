from fastapi import FastAPI
from fix_engine import generate_fixes

app = FastAPI(title="FixSuggest")

from fastapi.middleware.cors import CORSMiddleware

# ... après l'instanciation de app = FastAPI() ...

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Autorise ton frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/suggest-fixes")
async def suggest_fixes(report: dict):
    return generate_fixes(report)