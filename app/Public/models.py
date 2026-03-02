from typing import List

from sqlalchemy import String, Boolean, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship, mapped_column
from app.database import Base
from datetime import date


class Publics(Base):
    __tablename__ = "public"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)
    deleted_at: Mapped[bool] = mapped_column(Boolean, nullable=False, default=None)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    like: Mapped[List["Likes"]] = relationship(backref="public", cascade="all, delete-orphan")

    author: Mapped["Users"] = relationship(back_populates="public")

    def __repr__(self):
        return f"<Public {self.title}>"


class Likes(Base):
    __tablename__ = "likes"

    public_id: Mapped[int] = mapped_column(
        ForeignKey("public.id"),
        primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True
    )


    public: Mapped["Publics"] = relationship(back_populates="like")
    user: Mapped["Users"] = relationship(back_populates="like")

    def __repr__(self):
        return f"<Like {self.public_id}>"
