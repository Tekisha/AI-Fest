from pydantic import BaseModel
from typing import List, Optional


class HintRequest(BaseModel):
    problem_name: str
    student_solution: str
    correct_solution: str
    tests: str


class HintResponse(BaseModel):
    hints: List[str]


class TopicLinkRequest(BaseModel):
    topic: str
    sites: List[str]
    max_results: Optional[int] = 1


class SearchResult(BaseModel):
    title: str
    url: str
    text: str


class TopicLinkResponse(BaseModel):
    results: List[SearchResult]
