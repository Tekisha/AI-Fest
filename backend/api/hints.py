from fastapi import APIRouter, HTTPException

from backend.get_hints import get_hints
from backend.schemas import HintResponse, HintRequest

router = APIRouter()


@router.get("/hints", response_model=HintResponse)
async def get_hints(request: HintRequest):
    try:
        hints = get_hints(request.problem_name, request.student_solution, request.correct_solution, request.tests)
        return HintResponse(hints=hints)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
