
from fastapi import APIRouter
from schemas import ProblemsResponse
from database import get_problems

router = APIRouter()

@router.get("/problems", response_model=ProblemsResponse)
async def get_all_problems():
    problems = get_problems()
    return ProblemsResponse(problems=problems)
