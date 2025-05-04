from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func

from app.db import Base

class TextSummary(Base):
    __tablename__ = "textsummary"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
