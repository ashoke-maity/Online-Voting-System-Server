from fastapi import FastAPI

from app.api.admin_routes import router as admin_router
from app.api.election_routes import router as election_router
from app.api.candidate_routes import router as candidate_router
from app.api.voter_routes import router as voter_router
from app.api.upload_doc_routes import router as document_router

app = FastAPI(
    title = "Smart Voting System API",
    description = "Backend API for the Smart Voting System using Face Recognition",
    version = "1.0.0"
)


app.include_router(admin_router)
app.include_router(election_router)
app.include_router(candidate_router)
app.include_router(voter_router)
app.include_router(document_router)


@app.get("/")
def root():
    return {"message": "Smart Voting System API is running successfully !"}
