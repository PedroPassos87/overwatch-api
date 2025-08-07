from pydantic import BaseModel

class HeroesBase(BaseModel):
    name: str
    hero: str
    role: str
    age: int

class HeroesCreate(HeroesBase):
    pass

class HeroesOut(HeroesBase):
    id: int

    class Config:
        orm_mode = True
