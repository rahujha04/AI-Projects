from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "project" : "CodeSage AI",
        "version" : "1.0.0",
        "status" : "running"
    }

@router.get("/health")
def health():
    return {
        "status" : "healthy"
    }