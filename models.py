from pydantic import BaseModel

class ProfileIn(BaseModel):
    name: str
    skills: str
    goals: str

class Profile(ProfileIn):
    id: str