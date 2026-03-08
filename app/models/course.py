from sqlalchemy import DateTime, Boolean, Column, Integer, Numeric, String, func, CheckConstraint
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    title = Column (String, index=True)
    code = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)

    __table_args__ = (
        CheckConstraint("capacity > 0", name="capacity_positive"),
    )
   
