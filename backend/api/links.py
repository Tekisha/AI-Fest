from fastapi import APIRouter, HTTPException
from backend.schemas import TopicLinkRequest, TopicLinkResponse, ProblemSearchRequest
from backend.get_links import get_topic_links, get_links_for_problem

router = APIRouter()


@router.get("/topic-links", response_model=TopicLinkResponse)
async def get_topic_links(request: TopicLinkRequest):
    try:
        links = get_topic_links(request.topic, request.sites, request.max_results)
        return TopicLinkResponse(links=links)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/problem-links", response_model=TopicLinkResponse)
async def get_problem_links(request: ProblemSearchRequest):
    try:
        links = get_links_for_problem(request.problem_name, request.correct_solution, request.tests, request.sites)
        return TopicLinkResponse(links=links)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
