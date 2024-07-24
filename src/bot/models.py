import enum

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core import Base


class RoleEnum(str, enum.Enum):

    admin = "Админ"
    volunteer = "Волонтер"


class UserRole(Base):
    __tablename__ = "user_roles"

    role: Mapped[RoleEnum] = mapped_column(
        default=RoleEnum.volunteer.value,
        server_default=RoleEnum.volunteer.value,
    )


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int]
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    tg_username: Mapped[str] = mapped_column(String(30), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(30))
    user_role_id: Mapped[int] = mapped_column(
        ForeignKey("user_roles.id", ondelete="RESTRICT"), nullable=False
    )

    user_role: Mapped["UserRole"] = relationship(back_populates="users")


class FoodType(Base):
    __tablename__ = "food_types"

    name: Mapped[str] = mapped_column(String(50))
    measurement_unit: Mapped[str] = mapped_column(String(20))


class EventEnum(str, enum.Enum):

    recieved_on_point = "Получил на точке сбора"
    recieved_from_volunteer = "Получил от другого волонтера"
    used_for_feeding = "Потратил на кормление"


class EventType(Base):
    __tablename__ = "event_types"

    type: Mapped[EventEnum]


class CollectingPoint(Base):
    __tablename__ = "collecting_points"

    point_id: Mapped[int]
    city: Mapped[str] = mapped_column(String(30))
    city_district: Mapped[str] = mapped_column(String(30), nullable=True)
    street: Mapped[str] = mapped_column(String(30), nullable=True)
    building_number: Mapped[str] = mapped_column(String(10), nullable=True)
    mobile_station: Mapped[bool] = mapped_column(nullable=True)


class Event(Base):
    """Общее событие передачи корма"""

    __tablename__ = "events"

    event_type_id: Mapped[int] = mapped_column(
        ForeignKey("event_types.id", ondelete="RESTRICT"), nullable=False
    )
    event_types: Mapped["EventType"] = relationship(back_populates="events")


class CollectingPointTransfer(Base):
    """Событие передачи корма волонтеру с точки сбора"""

    __tablename__ = "collecting_point_transfers"

    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )
    sender_id: Mapped[int] = mapped_column(
        ForeignKey("collecting_points.id", ondelete="RESTRICT"), nullable=False
    )
    receiver_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )
    food_type_id: Mapped[int] = mapped_column(
        ForeignKey("food_types.id", ondelete="RESTRICT"), nullable=False
    )
    quantity: Mapped[int]

    event: Mapped["Event"] = relationship(
        back_populates="collecting_point_transfer"
    )
    sender: Mapped["CollectingPoint"] = relationship(
        back_populates="transfers"
    )
    receiver: Mapped["User"] = relationship(
        back_populates="collecting_point_transfers"
    )


class VolunteerTransfer(Base):
    """Событие передачи корма волонтеру от другого волонтера"""

    __tablename__ = "volunteer_transfers"

    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )
    sender_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )
    receiver_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )
    food_type_id: Mapped[int] = mapped_column(
        ForeignKey("food_types.id", ondelete="RESTRICT"), nullable=False
    )
    quantity: Mapped[int]

    event: Mapped["Event"] = relationship(back_populates="volunteer_transfer")
    sender: Mapped["User"] = relationship(
        back_populates="volunteer_transfers_send", foreign_keys=[sender_id]
    )
    receiver: Mapped["User"] = relationship(
        back_populates="volunteer_transfers_recieved",
        foreign_keys=[receiver_id],
    )


class FeedingEvent(Base):
    """Событие использования корма на кормление"""

    __tablename__ = "feeding_events"

    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )
    sender_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )
    food_type_id: Mapped[int] = mapped_column(
        ForeignKey("food_types.id", ondelete="RESTRICT"), nullable=False
    )
    quantity: Mapped[int]

    event: Mapped["Event"] = relationship(back_populates="feeding_event")
    sender: Mapped["User"] = relationship(back_populates="feeding_events")


class EventImage(Base):
    __tablename__ = "event_images"

    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id", ondelete="CASCADE"),
        nullable=False,
    )
    image: Mapped[str] = mapped_column(String(100))

    event: Mapped["Event"] = relationship(back_populates="images")
