from sqlalchemy import Column, Integer, String
from ..database import Base

class HeroesModels(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    hero = Column(String, nullable=False)
    role = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
