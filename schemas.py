from pydantic import BaseModel
from typing import Optional

class CourseOut(BaseModel):
    id: str
    code: Optional[str]
    title: Optional[str]
    title_en: Optional[str]
    description: Optional[str]
    language: Optional[str]
    level: Optional[str]
    season: Optional[str]

    class Config:
        orm_mode = True
