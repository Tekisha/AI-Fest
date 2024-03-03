from fastapi import APIRouter, HTTPException

from schemas import HintResponse, HintRequest
from database import get_correct_solution, get_tests, get_problem_name
from get_hints import get_hints

router = APIRouter()


@router.get("/hints/{problem_id}", response_model=HintResponse)
async def get_hints_for_id(problem_id: str, request: HintRequest):
    problem_name = get_problem_name(problem_id)
    correct_solution = get_correct_solution(problem_id)
    tests = get_tests(problem_id)

    if problem_name is None or correct_solution is None or tests is None:
        raise HTTPException(status_code=404, detail="Problem not found")

    try:
        hints = get_hints(problem_name, request.student_solution, correct_solution, tests)
        return HintResponse(hints=hints)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
