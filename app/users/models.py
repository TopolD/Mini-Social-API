from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.Public.models import Likes


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str]

    public: Mapped[list["Publics"]] = relationship(back_populates="author")
    like_post: Mapped[list["Publics"]] = relationship(
        back_populates="like_by", secondary=Likes
    )

    def __repr__(self):
        return f"<User {self.email}>"
