from app.models.course import Course
from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime, timezone
from app.schemas.course import CourseCreate, CourseUpdate
from app.core.security import get_password_hash


class CourseService:

    @staticmethod
    def get_course(db_session: Session, course_id: UUID):
        return db_session.query(Course).filter(
            Course.id == course_id,
            Course.deleted_at == None
        ).first()
    
    @staticmethod
    def update_course(db_session: Session, course_id: UUID,  course_update: CourseUpdate):
        course = db_session.query(Course).filter(
            Course.id == course_id,
            Course.deleted_at == None
        ).first()
    
        if not course:
            return None
        
        update_data = course_update.model_dump(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(course, key, value)
        
        db_session.add(course)
        db_session.commit()
        db_session.refresh(course)

        return course
    

    @staticmethod
    def course_status (db_session: Session, course_id: UUID, is_active: bool):
        course = db_session.query(Course).filter(
            Course.id == course_id,
            Course.deleted_at == None
        ).first()

        if not course:
            return None

        course.is_active = is_active

        
        db_session.add(course)
        db_session.commit()
        db_session.refresh(course)

        return course
    
    @staticmethod
    def soft_delete_course(db_session: Session, course_id: UUID):
        course = db_session.query(Course).filter(
            Course.id == course_id,
            Course.deleted_at == None
        ).first()

        if not course:
            return None

        course.deleted_at = datetime.now(timezone.utc)
        db_session.commit()
        db_session.refresh(course)
        return course