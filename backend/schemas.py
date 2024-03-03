from pydantic import BaseModel
from typing import List, Optional


class HintRequest(BaseModel):
    student_solution: str


class HintResponse(BaseModel):
    hints: List[str]


class TopicLinkRequest(BaseModel):
    topic: str
    sites: List[str]
    max_results: Optional[int] = 1


class LinkResult(BaseModel):
    title: str
    url: str
    text: str


class TopicLinkResponse(BaseModel):
    links: List[LinkResult]


class ProblemSearchRequest(BaseModel):
    problem_name: str
    correct_solution: str
    tests: str
    sites: List[str]


class ProblemItem(BaseModel):
    id: str
    problem_name: str


class ProblemsResponse(BaseModel):
    problems: List[ProblemItem]
