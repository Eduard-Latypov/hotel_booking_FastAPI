from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

# from src.bookings.models import Bookings


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]

    def __str__(self):
        return f"Пользователь {self.email}"
