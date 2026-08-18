from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

from .core.config import settings
from .routers.books import router as books_router


app = FastAPI(
    debug=settings.debug
)


@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "status_code": exc.status_code,
                "message": exc.detail,
                "path": str(request.url)
            }
        }
    )


@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "status_code": 500,
                "message": "Internal server error",
                "path": str(request.url)
            }
        }
    )


@app.get("/")
def home():
    return {
        "message": "BookVerse API"
    }


app.include_router(books_router)