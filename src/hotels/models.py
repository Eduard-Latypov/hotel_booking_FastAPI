from typing import Any

from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int] = mapped_column(nullable=False)

    def __str__(self):
        return f"Отель {self.name} {self.location[:30]}"
