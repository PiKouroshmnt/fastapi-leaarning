from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema, SummarySchema
from app.db import DB

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema,db: DB = Depends()) -> SummaryResponseSchema:
    summary_id = await crud.post(payload,db)

    response_object = {"id": summary_id, "url": payload.url}
    return response_object


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int,db: DB = Depends()) -> SummarySchema:
    summary = await crud.get(id,db)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary


@router.get("/", response_model=List[SummarySchema])
async def read_all_summaries(db: DB = Depends()) -> List[SummarySchema]:
    summaries = await crud.get_all(db)
    return summaries
