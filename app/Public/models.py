from sqlalchemy import String, Boolean, Date, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from app.database import Base
from datetime import date


class Publics(Base):
    __tablename__ = "public"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    like: Mapped[bool] = mapped_column(Boolean, default=False)
    dislike: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)
    deleted_at: Mapped[bool] = mapped_column(Boolean, nullable=False)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    owner: Mapped["User"] = relationship(back_populates="public")

    def __repr__(self):
        return f"<Public {self.title}>"