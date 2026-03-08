from pydantic import BaseModel, ConfigDict #confirm field
from decimal import Decimal
from datetime import datetime
from typing import Annotated, Optional
from uuid import UUID


class EnrollmenteBase(BaseModel):
    course_id: UUID 
    

class EnrollmentCreate(EnrollmenteBase):
    pass

class EnrollmentRead(EnrollmenteBase):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


 