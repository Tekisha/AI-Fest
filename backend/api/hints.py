from fastapi import APIRouter

from .. import schemas
from ..get_hints import get_hints
from ..schemas import HintResponse

router = APIRouter()


@router.post("/hints", response_model=HintResponse)
async def get_hints(request: schemas.HintRequest):
    hints = get_hints(request.problem_name, request.student_solution, request.correct_solution, request.tests)
    return HintResponse(hints=hints)
