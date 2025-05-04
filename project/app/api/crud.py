import logging
from typing import List, Union

from sqlalchemy.future import select
from app.models.pydantic import SummaryPayloadSchema
from app.models.sqlalchemy import TextSummary

log = logging.getLogger("uvicorn")


async def post(payload: SummaryPayloadSchema, db) -> int:
    try:
        summary = TextSummary(
            url=payload.url,
            summary="dummy summary",
        )
        db.save(summary)
        await db.commit()
        await db.refresh(summary)
        return summary.id
    except Exception as e:
        log.error(f"Error saving summary: {e}")
        raise


async def get(id: int,db) -> Union[dict, None]:
    summary = await db.get(TextSummary, id)
    return summary.scalar_one_or_none()


async def get_all(db) -> List:
    summaries = db.execute(select(TextSummary)).scalars().all()
    return summaries
