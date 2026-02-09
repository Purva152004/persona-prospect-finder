from pydantic import BaseModel
from typing import Optional

class PersonaInput(BaseModel):
    first_name: Optional[str] = "-"
    last_name: Optional[str] = "-"
    jobTitle: str
    company: Optional[str] = "-"
    location: str
    industry: str
    experience: int
    profile_url: Optional[str] = "-"
    email: Optional[str] = "-"
    phone: Optional[str] = "-"
