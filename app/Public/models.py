from typing import List

from sqlalchemy import String, Boolean, Date, ForeignKey, UniqueConstraint, Column, Integer, Table
from sqlalchemy.orm import Mapped, relationship, mapped_column
from app.database import Base
from datetime import date


likes = Table(
    "likes",
    Base.metadata,
    Base.metadata,
    Column("public_id", Integer, ForeignKey("public.id")),
    Column("user_id", Integer, ForeignKey("users.id")),

)




class Publics(Base):
    __tablename__ = "public"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)
    deleted_at: Mapped[bool] = mapped_column(Boolean, nullable=False, default=None)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    like_by: Mapped[List["Users"]] = relationship(back_populates="like_post", secondary=likes,cascade="all, delete-orphan")

    author: Mapped["Users"] = relationship(back_populates="public")

    def __repr__(self):
        return f"<Public {self.title}>"

