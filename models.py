from sqlalchemy import Column, String
from database import Base

class Course(Base):
    __tablename__ = "courses"
    id = Column(String, primary_key=True, index=True)  # e.g. 'ke_langtfagnumer'
    code = Column(String, index=True)                  # e.g. 'ke_stuttfagnumer'
    title = Column(String)
    title_en = Column(String)
    description = Column(String)
    language = Column(String)
    level = Column(String)
    season = Column(String)
