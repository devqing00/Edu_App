from sqlalchemy import Boolean, DateTime, Column, Integer, ForeignKey, Numeric, String, func, UniqueConstraint
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
   
    user = relationship("User")
    course = relationship("Course")


    __table_args__ = (
        UniqueConstraint("user_id", "course_id", name="unique_enrollment"),
    )