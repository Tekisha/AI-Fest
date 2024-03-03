from fastapi import APIRouter, HTTPException
from schemas import TopicLinkRequest, TopicLinkResponse, ProblemSearchRequest
from get_links import get_topic_links, get_links_for_problem
from database import get_correct_solution, get_tests, get_problem_name
from constants import sites
from utils import retry

router = APIRouter()


@router.get("/topic-links", response_model=TopicLinkResponse)
async def get_topic_links(request: TopicLinkRequest):
    try:
        links = get_topic_links(request.topic, request.sites, request.max_results)
        return TopicLinkResponse(links=links)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/problem-links/{problem_id}", response_model=TopicLinkResponse)
async def get_problem_links(problem_id: str):
    problem_name = get_problem_name(problem_id)
    correct_solution = get_correct_solution(problem_id)
    tests = get_tests(problem_id)

    if problem_name is None or correct_solution is None or tests is None:
        raise HTTPException(status_code=404, detail="Problem not found")

    try:
        links = retry(get_links_for_problem, problem_name, correct_solution, tests, sites)
        return TopicLinkResponse(links=links)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
