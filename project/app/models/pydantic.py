from pydantic import BaseModel


class SummarySchema(BaseModel):
    id: int
    url: str
    summary: str


class SummaryPayloadSchema(BaseModel):
    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int

