from pydantic import BaseModel
from typing import Optional, List

class PersonaInput(BaseModel):
    jobTitle: str
    experience: int
    location: str
    industry: str
    keywords: Optional[List[str]] = []

class ProspectOut(BaseModel):
    first_name: str
    last_name: str
    title: str
    company: str
    location: str
    industry: str
    experience: int
    profile_url: str
    email: str
    phone: str
    score: int
    reason: str
    source: str
