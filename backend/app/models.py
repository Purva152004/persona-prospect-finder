from sqlalchemy import Column, Integer, String
from database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    industry = Column(String)
    experience = Column(Integer)
    profile_url = Column(String)
    email = Column(String)
    phone = Column(String)
