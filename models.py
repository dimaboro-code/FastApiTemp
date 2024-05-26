from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# API models - pydantic
class APIClientData(BaseModel):
    name: str | None = None
    phone: int | None = None


class APIClient(BaseModel):
    client_id: int
    message: str
    time: datetime
    additional_fields: APIClientData


# Database models - SQLAlchemy
class Base(DeclarativeBase):
    pass


class DBClient(Base):
    """

    """
    __tablename__ = 'client'
    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int]
    message: Mapped[str]
    time: Mapped[datetime]
    name: Mapped[Optional[str]]
    phone: Mapped[Optional[int]]

    def __repr__(self) -> str:
        return f"User(id={self.client_id!r}, message={self.message!r}, name={self.name!r})"
