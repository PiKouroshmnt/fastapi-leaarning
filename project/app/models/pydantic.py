from pydantic import BaseModel


class SummarySchema(BaseModel):
    id: int
    url: str
    summary: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "url": "https://example.com",
                "summary": "This is a summary of the content.",
            }
        }


class SummaryPayloadSchema(BaseModel):
    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int

    class Config:
        json_schema_extra = {
            "example": {
                "url": "https://example.com",
                "id": 1,
            }
        }

