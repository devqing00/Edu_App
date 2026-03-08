from sqlalchemy import Boolean, Column, Integer, String, func, DateTime
from datetime import datetime, timezone
from enum import Enum
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "student"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    name = Column (String, index=True)
    role = Column(String, default=UserRole.USER.value)
    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)
    