from typing import List

from sqlalchemy.orm import Mapped, relationship, mapped_column
from app.database import Base

class Users(Base):
    __tablename__ = "users"


    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str]

    public:Mapped[List["Publics"]] = relationship(back_populates="author")
    like: Mapped[List["Likes"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"<User {self.email}>"