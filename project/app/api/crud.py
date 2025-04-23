import logging
from typing import List, Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary

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


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries
