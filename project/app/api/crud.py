from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary

import logging
log = logging.getLogger("uvicorn")

async def post(payload: SummaryPayloadSchema) -> int:
    try:
        summary = TextSummary(
            url=payload.url,
            summary="dummy summary",
        )
        await summary.save()
        return summary.id
    except Exception as e:
        log.error(f"Error saving summary: {e}")
        raise
