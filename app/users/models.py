from typing import List

from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.Public.models import likes
from app.database import Base

class Users(Base):
    __tablename__ = "users"


    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str]

    public:Mapped[List["Publics"]] = relationship(back_populates="author")
    like_post: Mapped[List["Publics"]] = relationship(back_populates="like_by",secondary=likes)

    def __repr__(self):
        return f"<User {self.email}>"