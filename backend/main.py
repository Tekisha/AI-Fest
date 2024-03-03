from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.hints import router as hint_router
from backend.settings import settings

app = FastAPI(title=settings.project_name, version=settings.version)

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hint_router, prefix="/api", tags=["hints"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.1", port=8000)

