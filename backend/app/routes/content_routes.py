from fastapi import APIRouter, HTTPException, Request

from backend.app.models.request_models import ContentRequest
from backend.app.services.openai_service import generate_content
from backend.app.utils.validator import validate_category
from backend.app.middleware.rate_limit import is_rate_limited
from backend.app.utils.logger import logger

router = APIRouter()


@router.post("/generate")
async def generate(request_data: ContentRequest, request: Request):

    client_ip = request.client.host

    if is_rate_limited(client_ip):
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please wait."
        )

    if not validate_category(request_data.category):
        raise HTTPException(
            status_code=400,
            detail="Invalid category selected."
        )

    try:

        result = generate_content(
            category=request_data.category,
            topic=request_data.topic,
            audience=request_data.audience,
            tone=request_data.tone
        )

        logger.info(
            f"Generated content for {request_data.category}"
        )

        return {
            "success": True,
            "content": result
        }

    except Exception as e:

        logger.error(str(e))

        return {
            "success": False,
            "error": str(e)
        }