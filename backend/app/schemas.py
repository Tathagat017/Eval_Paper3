from pydantic import BaseModel,Field
from typing import Optional,List

class CreateUserRequest(BaseModel):
    name:str = Field(repr=True)
    email:str
    age:int
    height:int
    weight:int
    fitness_goals:List[Optional[str]]
    medical_conditions:List[Optional[str]]
    activity_level:int
    
class UserResponseRequest(CreateUserRequest):
    id:int 
    
class AskRequest(BaseModel):
    question: str
    
class RAGResponse(AskRequest):
    answer:str