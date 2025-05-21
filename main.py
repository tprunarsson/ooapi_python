from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db, Base, engine
from models import Course
from schemas import CourseOut

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="OOAPI Courses Endpoint Example")

@app.get("/courses", response_model=List[CourseOut])
def list_courses(
    year: Optional[str] = Query(None),
    season: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    limit: int = 20,
    offset: int = 0
):
    query = db.query(Course)
    if year:
        query = query.filter(Course.id.like(f"{year}%"))
    if season:
        query = query.filter(Course.season == season)
    return query.offset(offset).limit(limit).all()

@app.get("/courses/{course_id}", response_model=CourseOut)
def get_course(course_id: str, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
