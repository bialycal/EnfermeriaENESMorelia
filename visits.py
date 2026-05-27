from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_visits():
    return {"message": "Visitas OK"}

