from datetime import date

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

Likes = Table(
    "likes",
    Base.metadata,
    Base.metadata,
    Column("public_id", Integer, ForeignKey("public.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
)


class Publics(Base):
    __tablename__ = "public"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)
    deleted_at: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    like_by: Mapped[list["Users"]] = relationship(
        back_populates="like_post", secondary=Likes
    )

    author: Mapped["Users"] = relationship(back_populates="public")

    def __repr__(self):
        return f"<Public {self.title}>"
