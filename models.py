from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id: Mapped[int]= mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)